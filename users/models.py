# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/models.py

from django.db import models
from django.conf import settings

from warehouses.models import Warehouse

class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
    


class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profile")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    
    # --- NEW: Granular Access Control (The "Tick Boxes") ---
    accessible_departments = models.ManyToManyField(
        Department, 
        blank=True, 
        related_name="accessed_by_employees",
        help_text="Tick the departments this employee is allowed to manage/view."
    )
    
    accessible_warehouses = models.ManyToManyField(
        Warehouse, 
        blank=True, 
        related_name="accessed_by_employees",
        help_text="Tick the warehouses this employee is allowed to operate in."
    )
    employee_code = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_code} - {self.user.username}"



class Role(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class EmployeeRole(models.Model):

    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE,
        related_name="roles",
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="employees",
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = (
            "employee",
            "role",
        )

    def __str__(self):
        return (
            f"{self.employee} - {self.role}"
        )
    

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="customer_profile"
    )
    company_name = models.CharField(max_length=200, blank=True)
    billing_address = models.TextField(blank=True)
    shipping_address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer: {self.user.username} - {self.company_name}"