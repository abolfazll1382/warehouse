import logging

from celery import shared_task

from apps.common.tasks import safe_delay

logger = logging.getLogger(__name__)


@shared_task
def notify_low_stock(item_id: int):
    """
    Fired from services.inventory_item_issue when a movement drops an item
    to/below its reorder threshold. Stubbed as a log line — swap in a real
    email/Slack webhook once you've got somewhere to send it.
    """
    from apps.inventory.models import InventoryItem

    try:
        item = InventoryItem.objects.get(id=item_id)
    except InventoryItem.DoesNotExist:
        return
    logger.warning(
        "Low stock: %s (%s) at %s %s, threshold is %s",
        item.name, item.sku, item.quantity, item.unit, item.reorder_threshold,
    )


@shared_task
def check_all_low_stock():
    """Scheduled via Celery Beat (see admin > Periodic tasks) as a daily
    sweep, independent of whatever movements happen to trigger the check
    above — catches items that drift low without a recent transaction."""
    from apps.inventory.models import InventoryItem

    low_ids = [i.id for i in InventoryItem.objects.all() if i.quantity <= i.reorder_threshold]
    for item_id in low_ids:
        safe_delay(notify_low_stock, item_id=item_id)
    return f"{len(low_ids)} item(s) at or below reorder threshold"
