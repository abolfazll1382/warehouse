# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/user_group.py

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserGroupSerializer(serializers.Serializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True
    )

    def update(self, instance, validated_data):
        groups = validated_data["groups"]
        instance.groups.set(groups)
        return instance