# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/services/stock.py

from django.db import transaction
from django.core.exceptions import ValidationError

from inventory.models import StockMovement


@transaction.atomic
def process_stock_movement(
    inventory,
    movement_type,
    quantity,
    performed_by=None,
    notes="",
):
    """
    Update inventory quantity and create movement atomically.
    """

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    if movement_type == StockMovement.MovementType.PURCHASE:
        inventory.quantity += quantity

    elif movement_type == StockMovement.MovementType.RETURN:
        inventory.quantity += quantity

    elif movement_type in (
        StockMovement.MovementType.SALE,
        StockMovement.MovementType.ADJUSTMENT,
    ):
        if inventory.quantity < quantity:
            raise ValidationError(
                f"Not enough stock. Available: {inventory.quantity}"
            )

        inventory.quantity -= quantity

    else:
        raise ValidationError(
            f"Unsupported movement type: {movement_type}"
        )

    inventory.save()

    movement = StockMovement.objects.create(
        inventory=inventory,
        movement_type=movement_type,
        quantity=quantity,
        performed_by=performed_by,
        notes=notes,
    )

    return movement