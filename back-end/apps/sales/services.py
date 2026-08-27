from django.db import transaction

from apps.accounts.models import User
from apps.common.exceptions import ServiceError
from apps.inventory import services as inventory_services
from apps.sales.models import Customer, Invoice, InvoiceLineItem


@transaction.atomic
def sales_invoice_create(*, customer: Customer, date, line_items: list[dict], actor: User) -> Invoice:
    """
    The 'ثبت فروش' flow: create the invoice + its line items, and issue the
    matching quantity out of inventory for each line. Selling something IS
    a stock-out event, so this reuses inventory's own service instead of
    mutating InventoryItem.quantity a second, disconnected way — one code
    path owns "how does stock change", regardless of who's asking.

    If any line fails (e.g. not enough stock), the whole invoice rolls back —
    you never end up with a half-fulfilled invoice.
    """
    if not line_items:
        raise ServiceError("An invoice needs at least one line item.")

    invoice = Invoice.objects.create(customer=customer, date=date)

    for line in line_items:
        item = line["item"]
        quantity = line["quantity"]
        unit_price = line["unit_price"]

        InvoiceLineItem.objects.create(invoice=invoice, item=item, quantity=quantity, unit_price=unit_price)
        inventory_services.inventory_item_issue(
            item=item,
            quantity=quantity,
            reason="sale",
            actor=actor,
            reference=invoice.invoice_number,
        )

    return invoice
