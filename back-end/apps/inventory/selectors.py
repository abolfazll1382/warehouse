"""
Read-only queries. Kept separate from services.py so a viewset's
get_queryset() can stay a one-liner and every place that needs "give me the
items list" builds it the same way (same select_related, same default
ordering) instead of every view re-inventing the query.
"""

from apps.inventory.models import InventoryItem, StockMovement


def inventory_item_list(*, category_id: int | None = None):
    qs = InventoryItem.objects.select_related("category")
    if category_id:
        qs = qs.filter(category_id=category_id)
    return qs


def stock_movement_list(*, item_id: int | None = None):
    qs = StockMovement.objects.select_related("item", "actor")
    if item_id:
        qs = qs.filter(item_id=item_id)
    return qs
