# MY_DJANGO PROJECTS TRAINING/warehouse_erp/transfer/services/transfer.py

from django.db import transaction
from django.core.exceptions import ValidationError

from inventory.models import Inventory, StockMovement
from inventory.services.stock import process_stock_movement
from transfer.models import Transfer


@transaction.atomic
def process_transfer(
    source_warehouse,
    destination_warehouse,
    product,
    quantity,
    performed_by,
    notes="",
):
    if source_warehouse == destination_warehouse:
        raise ValidationError(
            "Source and destination warehouses cannot be the same."
        )

    source_inventory = Inventory.objects.get(
        warehouse=source_warehouse,
        product=product,
    )

    destination_inventory, _ = Inventory.objects.get_or_create(
        warehouse=destination_warehouse,
        product=product,
        defaults={
            "quantity": 0,
        },
    )

    if source_inventory.quantity < quantity:
        raise ValidationError(
            f"Not enough stock. Available: {source_inventory.quantity}"
        )

    # Transfer OUT
    process_stock_movement(
        inventory=source_inventory,
        movement_type=StockMovement.MovementType.ADJUSTMENT,
        quantity=quantity,
        performed_by=performed_by,
        notes=f"Transfer OUT: {notes}",
    )

    # Transfer IN
    process_stock_movement(
        inventory=destination_inventory,
        movement_type=StockMovement.MovementType.PURCHASE,
        quantity=quantity,
        performed_by=performed_by,
        notes=f"Transfer IN: {notes}",
    )

    transfer = Transfer.objects.create(
        source_warehouse=source_warehouse,
        destination_warehouse=destination_warehouse,
        product=product,
        quantity=quantity,
        performed_by=performed_by,
        notes=notes,
    )

    return transfer