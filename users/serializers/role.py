# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/role.py

from rest_framework import serializers

from users.models import Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "description",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )