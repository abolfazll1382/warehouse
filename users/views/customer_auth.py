# users/views/customer_auth.py

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import VerificationCode
from users.serializers.customer_auth import (
    CustomerRegistrationSerializer,
    ResendVerificationSerializer,
    VerifyEmailSerializer,
)
from users.services.verification import (
    send_verification_code,
    verify_code,
)
from users.throttles import OTPRateThrottle

User = get_user_model()


class CustomerRegistrationView(GenericAPIView):
    """
    POST /api/register/

    Public endpoint (AllowAny). Creates an INACTIVE customer account and
    emails a 6-digit OTP. The account activates only after POST /api/verify/.
    """
    permission_classes = [AllowAny]
    serializer_class = CustomerRegistrationSerializer
    throttle_classes = [OTPRateThrottle]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "message": (
                    "Account created. A verification code has been sent to "
                    f"{user.email}. Verify your email to activate the account."
                ),
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )


class VerifyEmailView(GenericAPIView):
    """
    POST /api/verify/

    Body: {"email": "...", "code": "123456"}
    On success the user is activated and is_email_verified=True.
    """
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailSerializer
    throttle_classes = [OTPRateThrottle]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data["email"])

        try:
            verify_code(
                user,
                serializer.validated_data["code"],
            )
        except ValidationError as e:
            return Response(
                {"error": "; ".join(e.messages)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Email verified. Your account is now active."},
            status=status.HTTP_200_OK,
        )


class ResendVerificationView(GenericAPIView):
    """
    POST /api/resend/

    Body: {"email": "..."}
    Issues a fresh OTP for an unverified account.
    """
    permission_classes = [AllowAny]
    serializer_class = ResendVerificationSerializer
    throttle_classes = [OTPRateThrottle]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data["email"])

        if user.is_email_verified:
            return Response(
                {"message": "This email is already verified."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        send_verification_code(user)

        return Response(
            {"message": "A new verification code has been sent."},
            status=status.HTTP_200_OK,
        )
