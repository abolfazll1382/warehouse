# sales/models.py

from django.db import models
from django.conf import settings
from products.models import Product
from warehouses.models import Warehouse
from users.models import CustomerProfile

class SalesOrder(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"           # Customer placed the order
        PROCESSING = "PROCESSING", "Processing"  # Warehouse staff is packing it
        SHIPPED = "SHIPPED", "Shipped"           # It left the warehouse
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    customer = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT, related_name="orders")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="sales_orders")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    # Who packed/shipped this order? (Null until an employee starts processing it)
    processed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="processed_orders"
    )
    
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SO-{self.id} ({self.customer.company_name})"


class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.sales_order} - {self.product.name} (x{self.quantity})"