# users/serializers/customer_auth.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import CustomerProfile
import re

User = get_user_model()

class CustomerRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    
    # Customer Profile Fields
    company_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField()

    def validate_phone(self, value):
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
        # 1. Extract profile data
        company_name = validated_data.pop('company_name', '')
        phone = validated_data.pop('phone', '')

        # 2. Create the User (is_staff=False by default, which is perfect for customers)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # 3. Create the Customer Profile
        CustomerProfile.objects.create(
            user=user,
            company_name=company_name,
            phone=phone
        )

        return user