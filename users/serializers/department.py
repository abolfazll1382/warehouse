# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/department.py

from rest_framework import serializers

from users.models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
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