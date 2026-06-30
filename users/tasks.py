# users/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_otp_email(self, user_id, code, purpose):
    """
    Email the OTP verification code to the user.

    Runs asynchronously via Celery. Retries up to 3 times on failure.
    """
    from django.contrib.auth import get_user_model

    User = get_user_model()

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        # Nothing to do if the user vanished between enqueue and run.
        return None

    if purpose == "RESET":
        subject = "Your password reset code"
        verb = "reset your password"
    else:
        subject = "Verify your email — Warehouse ERP"
        verb = "activate your account"

    message = (
        f"Hi {user.username},\n\n"
        f"Use the code below to {verb}.\n\n"
        f"    {code}\n\n"
        f"This code expires in {settings.OTP_EXPIRY_MINUTES} minutes.\n"
        f"If you didn't request this, you can safely ignore this email.\n"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
    return {"user": user.username, "purpose": purpose}
