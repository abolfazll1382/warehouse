# users/serializers/customer_auth.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import CustomerProfile, User
import re

User = get_user_model()


class CustomerRegistrationSerializer(serializers.Serializer):
    """
    Registers a CUSTOMER account.

    The user is created with is_active=False; an OTP code is emailed and the
    account only activates after the code is verified (see VerifyEmailView).
    This is exactly the "don't trust the email/phone until proven" rule.
    """

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    # Customer Profile Fields
    company_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField()

    def validate_phone(self, value):
        # NOTE: Stage 4 will replace this with a shared phonenumbers validator.
        pattern = r"^(09\d{9}|\+989\d{9})$"
        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid phone number format.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def create(self, validated_data):
        company_name = validated_data.pop('company_name', '')
        phone = validated_data.pop('phone', '')

        # 1. Create the user INACTIVE until the email is verified.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False,
            user_type=User.UserType.CUSTOMER,
            phone=phone,
        )

        # 2. Create the Customer Profile.
        CustomerProfile.objects.create(
            user=user,
            company_name=company_name,
            phone=phone,
        )

        # 3. Issue the OTP and email it (async via Celery).
        #    Importing here avoids a circular import at module load.
        from users.services.verification import send_verification_code
        send_verification_code(user)

        return user


class VerifyEmailSerializer(serializers.Serializer):
    """Submitted by the user to confirm they own the email they registered."""

    email = serializers.EmailField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account found with this email.")
        return value


class ResendVerificationSerializer(serializers.Serializer):
    """Request a fresh OTP for an existing unverified account."""

    email = serializers.EmailField()
