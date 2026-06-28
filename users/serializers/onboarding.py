# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/onboarding.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import (
    Department,
    Role,
    EmployeeProfile,
)

import re

User = get_user_model()


class EmployeeOnboardingSerializer(
    serializers.Serializer
):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    employee_code = serializers.CharField()

    phone = serializers.CharField()

    hire_date = serializers.DateField()

    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all()
    )

    def validate_employee_code(
        self,
        value,
    ):
        if EmployeeProfile.objects.filter(
            employee_code=value
        ).exists():
            raise serializers.ValidationError(
                "Employee code already exists."
            )

        return value
    
    def validate_email(
        self,
        value,
    ):
        if User.objects.filter(
            email=value
        ).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value
    
    def validate_username(
        self,
        value,
    ):
        if User.objects.filter(
            username=value
        ).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )

        return value
    
    def validate_phone(
        self,
        value,
    ):
        pattern = (
            r"^(09\d{9}|\+989\d{9})$"
        )

        if not re.match(
            pattern,
            value,
        ):
            raise serializers.ValidationError(
                "Invalid phone number."
            )

        return value
    
    # def validate_password(
    #     self,
    #     value,
    # ):
    #     if len(value) < 8:
    #         raise serializers.ValidationError(
    #             "Password must be at least 8 characters."
    #         )

    #     return value