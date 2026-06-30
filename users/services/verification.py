# users/services/verification.py

"""
OTP generation + verification logic.

Flow:
  register -> create user (is_active=False) -> send_verification_code()
           -> enqueue celery task that emails the 6-digit code
  verify   -> verify_code(user, code) -> on success: is_active=True,
             is_email_verified=True
"""

import secrets

from django.conf import settings
from django.contrib.auth.hashers import (
    check_password,
    make_password,
)
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from users.models import VerificationCode
from users.tasks import send_otp_email


def _generate_code():
    """Return a cryptographically random 6-digit code as a string."""
    # 900000 possible codes; secrets is CSPRNG so not guessable.
    return f"{secrets.randbelow(1000000):06d}"


@transaction.atomic
def send_verification_code(user, *, purpose=VerificationCode.Purpose.REGISTER):
    """
    Generate a fresh OTP for `user`, persist it hashed, and enqueue the
    email-sending Celery task. Returns the plaintext code (for the console
    email backend / tests). Production callers should ignore the return.
    """
    # Invalidate any previous unused codes for this user+purpose so only the
    # newest one works.
    VerificationCode.objects.filter(
        user=user,
        purpose=purpose,
        is_used=False,
    ).update(is_used=True)

    code = _generate_code()
    expires_at = timezone.now() + timezone.timedelta(
        minutes=settings.OTP_EXPIRY_MINUTES
    )

    verification = VerificationCode.objects.create(
        user=user,
        purpose=purpose,
        code_hash=make_password(code),
        expires_at=expires_at,
    )

    # Fire-and-forget the email. send_otp_email.delay(...) runs on Celery.
    send_otp_email.delay(
        user_id=user.id,
        code=code,
        purpose=purpose,
    )

    return code


@transaction.atomic
def verify_code(user, code, *, purpose=VerificationCode.Purpose.REGISTER):
    """
    Validate `code` against the latest active code for `user`.

    On success: marks the code used, activates the user, sets
    is_email_verified=True. On failure raises ValidationError with a reason.
    """
    if not code:
        raise ValidationError("Verification code is required.")

    latest = (
        VerificationCode.objects.filter(
            user=user,
            purpose=purpose,
        )
        .order_by("-created_at")
        .first()
    )

    if latest is None:
        raise ValidationError("No verification code was issued.")

    if latest.is_used:
        raise ValidationError("This code has already been used. Request a new one.")

    if latest.attempts >= settings.OTP_MAX_ATTEMPTS:
        raise ValidationError("Too many attempts. Request a new code.")

    # Bump attempt counter BEFORE checking, to mitigate timing brute-force.
    latest.attempts += 1
    latest.save(update_fields=["attempts"])

    if timezone.now() > latest.expires_at:
        raise ValidationError("This code has expired. Request a new one.")

    if not check_password(code, latest.code_hash):
        remaining = settings.OTP_MAX_ATTEMPTS - latest.attempts
        raise ValidationError(
            f"Invalid code. {remaining} attempt(s) left."
        )

    # Success.
    latest.is_used = True
    latest.save(update_fields=["is_used"])

    # Use update_fields to avoid clobbering unrelated changes.
    user.is_active = True
    user.is_email_verified = True
    user.save(update_fields=["is_active", "is_email_verified"])

    return user
