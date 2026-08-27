from django.db import models

from apps.common.models import TimeStampedModel


class Customer(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def total_purchases(self):
        from django.db.models import DecimalField, ExpressionWrapper, F, Sum

        result = self.invoices.filter(status="completed").aggregate(
            total=Sum(
                ExpressionWrapper(
                    F("line_items__quantity") * F("line_items__unit_price"),
                    output_field=DecimalField(max_digits=14, decimal_places=0),
                )
            )
        )
        return result["total"] or 0


class Invoice(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    invoice_number = models.CharField(max_length=20, unique=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="invoices")
    date = models.DateField()
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.invoice_number

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new and not self.invoice_number:
            self.invoice_number = f"INV-{10000 + self.id}"
            super().save(update_fields=["invoice_number"])

    @property
    def amount(self):
        return sum((line.subtotal for line in self.line_items.all()), start=0)


class InvoiceLineItem(TimeStampedModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="line_items")
    item = models.ForeignKey("inventory.InventoryItem", on_delete=models.PROTECT, related_name="+")
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=14, decimal_places=0)

    def __str__(self):
        return f"{self.item.name} x{self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price
