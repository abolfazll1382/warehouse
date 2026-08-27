from rest_framework import serializers

from apps.hr.models import Employee, Payroll


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "full_name", "position", "department", "hire_date", "status", "user"]
        read_only_fields = ["id"]


class PayrollSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.full_name", read_only=True)
    net_pay = serializers.DecimalField(max_digits=14, decimal_places=0, read_only=True)

    class Meta:
        model = Payroll
        fields = [
            "id", "employee", "employee_name", "period",
            "base_salary", "insurance_deduction", "tax_deduction", "net_pay", "status",
        ]
        read_only_fields = ["id"]
