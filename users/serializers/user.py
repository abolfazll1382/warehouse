# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/user.py

from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "password",
        )

        read_only_fields = (
            "id",
        )

    def create(self, validated_data):

        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )