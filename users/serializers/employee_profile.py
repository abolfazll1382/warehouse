# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/serializers/employee_profile.py

from rest_framework import serializers

from users.models import EmployeeProfile


class EmployeeProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeProfile
        fields = (
            "id",
            "user",
            "department",
            "employee_code",
            "phone",
            "hire_date",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )