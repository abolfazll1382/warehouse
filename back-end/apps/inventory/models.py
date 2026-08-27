from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class InventoryItem(TimeStampedModel):
    class Status(models.TextChoices):
        IN_STOCK = "in_stock", "In stock"
        LOW_STOCK = "low_stock", "Low stock"
        OUT_OF_STOCK = "out_of_stock", "Out of stock"

    sku = models.CharField("SKU", max_length=32, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="items")
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=20, help_text="e.g. m, kg, pcs, roll")
    reorder_threshold = models.PositiveIntegerField(
        default=10, help_text="Quantity at/below which the item counts as low stock."
    )

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["category", "quantity"])]

    def __str__(self):
        return f"{self.sku} — {self.name}"

    @property
    def status(self) -> str:
        if self.quantity == 0:
            return self.Status.OUT_OF_STOCK
        if self.quantity <= self.reorder_threshold:
            return self.Status.LOW_STOCK
        return self.Status.IN_STOCK


class StockMovement(TimeStampedModel):
    """
    Append-only ledger of every change to an item's quantity. Both
    "add to warehouse" and "issue / remove" write here — they're the same
    event with opposite-signed quantity, which is what makes InventoryItem's
    running total auditable instead of just a mutable counter with no history.
    """

    class Reason(models.TextChoices):
        PURCHASE = "purchase", "Purchase receipt"
        SALE = "sale", "Sold to customer"
        INTERNAL_USE = "internal_use", "Used in production"
        DAMAGED = "damaged", "Damaged / scrapped"
        TRANSFER = "transfer", "Transferred between warehouses"
        RETURN = "return", "Returned to supplier"
        ADJUSTMENT = "adjustment", "Manual adjustment"

    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name="movements")
    quantity = models.IntegerField(help_text="Positive = stock in, negative = stock out.")
    reason = models.CharField(max_length=20, choices=Reason.choices)
    reference = models.CharField(max_length=64, blank=True, help_text="PO / invoice number, if any.")
    note = models.CharField(max_length=255, blank=True)
    actor = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, related_name="stock_movements"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        sign = "+" if self.quantity >= 0 else ""
        return f"{self.item.sku} {sign}{self.quantity} ({self.reason})"
