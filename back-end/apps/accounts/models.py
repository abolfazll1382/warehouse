from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.managers import UserManager


class User(AbstractUser):
    """
    Custom user model, in place from the start (swapping AUTH_USER_MODEL
    after the first migration means resetting the database — this avoids
    that entirely).

    `department` is what apps/common/permissions.IsDepartmentStaff checks,
    so it's the single source of truth for "who can touch this module".
    """

    class Department(models.TextChoices):
        MANAGEMENT = "management", "Management"
        HR = "hr", "Human Resources"
        PRODUCTION = "production", "Production"
        PURCHASING = "purchasing", "Purchasing"
        INVENTORY = "inventory", "Inventory"
        SALES = "sales", "Sales"
        FINANCE = "finance", "Finance"

    username = None
    email = models.EmailField("email address", unique=True)
    department = models.CharField(max_length=20, choices=Department.choices, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email

    @property
    def full_name(self) -> str:
        return self.get_full_name() or self.email
