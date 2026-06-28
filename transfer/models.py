# MY_DJANGO PROJECTS TRAINING/warehouse_erp/transfer/models.py

from django.conf import settings
from django.db import models

from warehouses.models import Warehouse
from products.models import Product


class Transfer(models.Model):
    source_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="outgoing_transfers",
    )

    destination_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="incoming_transfers",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField()

    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.product} "
            f"{self.source_warehouse} → "
            f"{self.destination_warehouse}"
        )