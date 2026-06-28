# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/employee_role.py

from rest_framework import serializers

from users.models import EmployeeRole


class EmployeeRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeRole

        fields = (
            "id",
            "employee",
            "role",
            "assigned_at",
        )

        read_only_fields = (
            "id",
            "assigned_at",
        )