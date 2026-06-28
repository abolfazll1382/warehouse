# users/serializers/permission.py

from django.contrib.auth.models import Permission
from rest_framework import serializers

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        # codename is the actual code (e.g., "add_transfer"), name is human-readable
        fields = ('id', 'name', 'codename') 

class UserPermissionAssignSerializer(serializers.Serializer):
    # This expects a list of Permission IDs: e.g., {"user_permissions": [1, 5, 12]}
    user_permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True
    )

    def update(self, instance, validated_data):
        permissions = validated_data["user_permissions"]
        # This replaces the user's current ticks with the new ones provided
        instance.user_permissions.set(permissions)
        return instance