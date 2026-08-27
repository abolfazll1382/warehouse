from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "full_name", "first_name", "last_name", "department", "phone_number"]
        read_only_fields = ["id", "email", "department"]


class ERPTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Identical to simplejwt's default except the response also carries the
    user's own profile — saves the frontend an extra round trip to /me/
    right after login, which is what most SPA/dashboard clients want.
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data
