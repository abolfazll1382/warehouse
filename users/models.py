# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from warehouses.models import Warehouse


class User(AbstractUser):
    """
    Custom user model.

    Every account is either a CUSTOMER (self-registers via the public
    storefront) or an EMPLOYEE (provisioned by the CEO through onboarding).
    Verification flags are set once the user proves ownership of their
    email/phone (OTP flow).
    """

    class UserType(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        EMPLOYEE = "EMPLOYEE", "Employee"

    # The default Django user.email is not unique; we need it unique so it
    # can double as a contact channel for OTP and (later) login.
    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
    )

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.CUSTOMER,
    )

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.user_type})"


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


class VerificationCode(models.Model):
    """
    A one-time OTP used to prove a user owns their email (signup / reset).

    The `code` is stored HASHED (never in plaintext) so a DB leak can't
    reveal usable codes. Codes expire after OTP_EXPIRY_MINUTES and are
    invalidated after OTP_MAX_ATTEMPTS wrong guesses.
    """

    class Purpose(models.TextChoices):
        REGISTER = "REGISTER", "Registration"
        RESET = "RESET", "Password reset"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="verification_codes",
    )
    purpose = models.CharField(
        max_length=10,
        choices=Purpose.choices,
        default=Purpose.REGISTER,
    )
    # Hashed 6-digit code (uses django.contrib.auth.hashers.make_password).
    code_hash = models.CharField(max_length=128)
    attempts = models.PositiveIntegerField(default=0)
    is_used = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "purpose"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.purpose} ({'used' if self.is_used else 'active'})"