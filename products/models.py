from django.db import models


class Product(models.Model):
    sku = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    unit = models.CharField(
        max_length=20,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
    )

    minimum_stock = models.PositiveIntegerField(
        default=0,
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
        return f"{self.sku} - {self.name}"