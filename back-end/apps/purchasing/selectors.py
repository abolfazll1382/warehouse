from apps.purchasing.models import PurchaseOrder, Supplier


def supplier_list(*, status: str | None = None):
    qs = Supplier.objects.all()
    if status:
        qs = qs.filter(status=status)
    return qs


def purchase_order_list(*, supplier_id: int | None = None, status: str | None = None):
    qs = PurchaseOrder.objects.select_related("supplier")
    if supplier_id:
        qs = qs.filter(supplier_id=supplier_id)
    if status:
        qs = qs.filter(status=status)
    return qs
