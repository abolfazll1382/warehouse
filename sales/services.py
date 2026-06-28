# sales/services.py

from django.db import transaction
from django.core.exceptions import ValidationError
from inventory.models import StockMovement, Inventory
from inventory.services.stock import process_stock_movement
from sales.models import SalesOrder

@transaction.atomic
def ship_sales_order(sales_order, performed_by):
    """
    Marks an order as SHIPPED and safely deducts inventory.
    Rolls back completely if there isn't enough stock!
    """
    if sales_order.status != SalesOrder.Status.PROCESSING:
        raise ValidationError("Only 'Processing' orders can be shipped.")

    # 1. Deduct all items from inventory
    for item in sales_order.items.all():
        # Find the inventory record for this warehouse and product
        inventory = Inventory.objects.filter(
            warehouse=sales_order.warehouse,
            product=item.product
        ).first()

        if not inventory:
            raise ValidationError(f"Product {item.product.name} does not exist in this warehouse.")

        # Re-use our rock-solid stock movement service!
        process_stock_movement(
            inventory=inventory,
            movement_type=StockMovement.MovementType.SALE,
            quantity=item.quantity,
            performed_by=performed_by,
            notes=f"Shipped SO-{sales_order.id}"
        )

    # 2. Update the order status
    sales_order.status = SalesOrder.Status.SHIPPED
    sales_order.processed_by = performed_by
    sales_order.save(update_fields=['status', 'processed_by', 'updated_at'])
    
    return sales_order