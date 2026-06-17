from django.conf import settings
from django.db import models


class Warehouse(models.Model):
    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
        unique=True,
    )

    address = models.TextField(
        blank=True,
    )

    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_warehouses",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.code} - {self.name}"