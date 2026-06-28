# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/services/onboarding.py

from django.contrib.auth import get_user_model
from django.db import transaction

from users.models import (
    EmployeeProfile,
    EmployeeRole,
    Role,
    Department,
)

User = get_user_model()


@transaction.atomic
def onboard_employee(
    *,
    username,
    email,
    password,
    department,
    employee_code,
    phone,
    hire_date,
    role,
):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    employee = EmployeeProfile.objects.create(
        user=user,
        department=department,
        employee_code=employee_code,
        phone=phone,
        hire_date=hire_date,
    )

    EmployeeRole.objects.create(
        employee=employee,
        role=role,
    )

    return employee