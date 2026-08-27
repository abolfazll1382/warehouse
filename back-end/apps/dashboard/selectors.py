"""
Read-only aggregation queries for the Overview page. No models of its own —
this app is purely a reporting layer over hr/production/purchasing/sales/
inventory/finance, which is why it only has selectors.py, no services.py.

Deliberately returns raw numbers and semantic `id`/`type` fields rather than
Persian labels or formatted strings — that's presentation, and belongs in
the frontend (which already owns exactly this mapping in lib/nav-config.ts
and lib/data/dashboard.ts), not baked into the API response.
"""

from datetime import date, timedelta

from django.db.models import DecimalField, ExpressionWrapper, F, Sum

from apps.hr.models import Employee
from apps.inventory.models import InventoryItem
from apps.purchasing.models import PurchaseOrder
from apps.sales.models import Invoice, InvoiceLineItem

MONEY = DecimalField(max_digits=14, decimal_places=0)


def _month_start(d: date) -> date:
    return d.replace(day=1)


def _next_month_start(d: date) -> date:
    # +32 days always lands in the following month regardless of length;
    # snapping to day=1 then normalizes it to that month's start.
    return (_month_start(d) + timedelta(days=32)).replace(day=1)


def _previous_month_start(d: date) -> date:
    return (_month_start(d) - timedelta(days=1)).replace(day=1)


def _sales_total(start: date, end: date) -> int:
    """Sum of completed invoice line items in [start, end)."""
    total = InvoiceLineItem.objects.filter(
        invoice__status="completed", invoice__date__gte=start, invoice__date__lt=end
    ).aggregate(total=Sum(ExpressionWrapper(F("quantity") * F("unit_price"), output_field=MONEY)))["total"]
    return total or 0


def _percent_change(current: float, previous: float) -> tuple[float, str]:
    if previous == 0:
        return (100.0 if current > 0 else 0.0), "up"
    change = (current - previous) / previous * 100
    return round(abs(change), 1), ("up" if change >= 0 else "down")


def kpi_summary(*, today: date | None = None) -> dict:
    today = today or date.today()
    this_month_start = _month_start(today)
    last_month_start = _previous_month_start(today)

    sales_this_month = _sales_total(this_month_start, _next_month_start(today))
    sales_last_month = _sales_total(last_month_start, this_month_start)
    sales_change, sales_trend = _percent_change(sales_this_month, sales_last_month)

    return {
        "kpis": [
            {
                "id": "monthly-sales",
                "value": sales_this_month,
                "change_percent": sales_change,
                "trend": sales_trend,
            },
            {"id": "stock-items", "value": InventoryItem.objects.count(), "change_percent": None, "trend": None},
            {
                "id": "active-employees",
                "value": Employee.objects.filter(status="active").count(),
                "change_percent": None,
                "trend": None,
            },
            {
                "id": "pending-orders",
                "value": PurchaseOrder.objects.filter(status__in=["pending", "processing"]).count(),
                "change_percent": None,
                "trend": None,
            },
        ]
    }


def monthly_trend(*, months: int = 7) -> list[dict]:
    """Last N calendar months of (sales total, invoice count), oldest
    first — the shape the RevenueChart component already expects."""
    month_starts = []
    cursor = _month_start(date.today())
    for _ in range(months):
        month_starts.append(cursor)
        cursor = _previous_month_start(cursor)
    month_starts.reverse()

    points = []
    for start in month_starts:
        end = _next_month_start(start)
        points.append(
            {
                "month": start.isoformat(),
                "sales": _sales_total(start, end),
                "orders": Invoice.objects.filter(date__gte=start, date__lt=end).count(),
            }
        )
    return points


def recent_transactions(*, limit: int = 7) -> list[dict]:
    """Merges Invoices (money in) and PurchaseOrders (money out) into one
    activity feed, newest first — mirrors the frontend's unified
    Transaction type instead of making the client merge two API calls."""
    invoices = Invoice.objects.select_related("customer").order_by("-date")[:limit]
    orders = PurchaseOrder.objects.select_related("supplier").order_by("-date")[:limit]

    entries = [
        {
            "id": f"invoice-{inv.pk}",
            "party": inv.customer.name,
            "description": f"Invoice {inv.invoice_number}",
            "date": inv.date.isoformat(),
            "amount": inv.amount,
            "direction": "in",
            "status": inv.status,
        }
        for inv in invoices
    ] + [
        {
            "id": f"po-{po.pk}",
            "party": po.supplier.name,
            "description": f"Purchase order {po.order_number}",
            "date": po.date.isoformat(),
            "amount": po.amount,
            "direction": "out",
            "status": po.status,
        }
        for po in orders
    ]
    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries[:limit]


def top_products(*, limit: int = 5) -> list[dict]:
    """Top-selling inventory items this month by revenue, with each one's
    share of the total — same shape as the frontend's TopProducts widget."""
    start = _month_start(date.today())

    rows = list(
        InvoiceLineItem.objects.filter(invoice__status="completed", invoice__date__gte=start)
        .values("item__id", "item__name", "item__category__name")
        .annotate(amount=Sum(ExpressionWrapper(F("quantity") * F("unit_price"), output_field=MONEY)))
        .order_by("-amount")[:limit]
    )
    total = sum(r["amount"] for r in rows) or 1

    return [
        {
            "id": r["item__id"],
            "name": r["item__name"],
            "category": r["item__category__name"],
            "amount": r["amount"],
            "share": round(float(r["amount"]) / float(total) * 100, 1),
        }
        for r in rows
    ]
