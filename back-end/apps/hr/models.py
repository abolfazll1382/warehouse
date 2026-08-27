from django.db import models

from apps.accounts.models import User
from apps.common.models import TimeStampedModel


class Employee(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="employee_profile",
        help_text="Linked only if this employee also has a system login.",
    )
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=20, choices=User.Department.choices)
    hire_date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Payroll(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="payroll_records")
    period = models.DateField(help_text="First day of the pay period month.")
    base_salary = models.DecimalField(max_digits=14, decimal_places=0)
    insurance_deduction = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    tax_deduction = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)

    class Meta:
        ordering = ["-period"]
        constraints = [
            models.UniqueConstraint(fields=["employee", "period"], name="unique_payroll_per_period")
        ]

    def __str__(self):
        return f"{self.employee.full_name} — {self.period:%Y-%m}"

    @property
    def net_pay(self):
        return self.base_salary - self.insurance_deduction - self.tax_deduction
