from django.db import transaction

from apps.accounts.models import User
from apps.common.exceptions import ServiceError
from apps.common.tasks import safe_delay
from apps.inventory.models import InventoryItem, StockMovement
from apps.inventory.tasks import notify_low_stock


@transaction.atomic
def inventory_item_receive(
    *, item: InventoryItem, quantity: int, reason: str, actor: User, reference: str = "", note: str = ""
) -> InventoryItem:
    """Add stock to a warehouse item — the 'افزودن کالا به انبار' flow."""
    if quantity <= 0:
        raise ServiceError("Quantity received must be positive.")

    item.quantity += quantity
    item.save(update_fields=["quantity", "updated_at"])
    StockMovement.objects.create(
        item=item, quantity=quantity, reason=reason, reference=reference, note=note, actor=actor
    )
    return item


@transaction.atomic
def inventory_item_issue(
    *, item: InventoryItem, quantity: int, reason: str, actor: User, reference: str = "", note: str = ""
) -> InventoryItem:
    """Remove stock from a warehouse item — the 'خروج / حذف کالا' flow."""
    if quantity <= 0:
        raise ServiceError("Quantity issued must be positive.")
    if quantity > item.quantity:
        raise ServiceError(f"Cannot issue {quantity} {item.unit}: only {item.quantity} in stock.")

    item.quantity -= quantity
    item.save(update_fields=["quantity", "updated_at"])
    StockMovement.objects.create(
        item=item, quantity=-quantity, reason=reason, reference=reference, note=note, actor=actor
    )

    if item.status in (InventoryItem.Status.LOW_STOCK, InventoryItem.Status.OUT_OF_STOCK):
        # Fire-and-forget: the API response shouldn't wait on — or fail
        # because of — a notification.
        safe_delay(notify_low_stock, item_id=item.id)

    return item
