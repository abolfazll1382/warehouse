from django.db import transaction
from django.core.exceptions import ValidationError

from inventory.models import Inventory
from inventory.models import StockMovement

from inventory.services.stock import (
    process_stock_movement,
)

from purchasing.models import (
    PurchaseOrder,
)


@transaction.atomic
def receive_purchase_order(
    purchase_order,
    warehouse,
    performed_by,
):
    if purchase_order.status == PurchaseOrder.Status.RECEIVED:
        raise ValidationError(
            "Purchase order already received."
        )

    for item in purchase_order.items.all():

        inventory, _ = Inventory.objects.get_or_create(
            warehouse=warehouse,
            product=item.product,
            defaults={
                "quantity": 0,
            },
        )

        process_stock_movement(
            inventory=inventory,
            movement_type=StockMovement.MovementType.PURCHASE,
            quantity=item.quantity,
            performed_by=performed_by,
            notes=f"PO-{purchase_order.id}",
        )

    purchase_order.status = (
        PurchaseOrder.Status.RECEIVED
    )

    purchase_order.save(
        update_fields=[
            "status",
        ]
    )