# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/services/approve.py

from django.core.exceptions import ValidationError
from django.db import transaction

from purchasing.models import PurchaseOrder


@transaction.atomic
def approve_purchase_order(
    purchase_order,
):
    if purchase_order.status != (
        PurchaseOrder.Status.DRAFT
    ):
        raise ValidationError(
            "Only draft purchase orders can be approved."
        )

    purchase_order.status = (
        PurchaseOrder.Status.APPROVED
    )

    purchase_order.save(
        update_fields=[
            "status",
        ]
    )

    return purchase_order