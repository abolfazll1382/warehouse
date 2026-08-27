from django.db.models import DecimalField, ExpressionWrapper, F, Q, Sum

from apps.sales.models import Customer, Invoice


def customer_list(*, status: str | None = None):
    """
    Annotates total_purchases in one query instead of every row hitting
    Customer.total_purchases individually (which would be an N+1 query on
    any list of more than one customer).
    """
    qs = Customer.objects.annotate(
        total_purchases_annotated=Sum(
            ExpressionWrapper(
                F("invoices__line_items__quantity") * F("invoices__line_items__unit_price"),
                output_field=DecimalField(max_digits=14, decimal_places=0),
            ),
            filter=Q(invoices__status="completed"),
        )
    )
    if status:
        qs = qs.filter(status=status)
    return qs


def invoice_list(*, customer_id: int | None = None, status: str | None = None):
    qs = Invoice.objects.select_related("customer").prefetch_related("line_items__item")
    if customer_id:
        qs = qs.filter(customer_id=customer_id)
    if status:
        qs = qs.filter(status=status)
    return qs
