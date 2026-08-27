from rest_framework import serializers

from apps.inventory.models import InventoryItem
from apps.sales.models import Customer, Invoice, InvoiceLineItem
from apps.sales.services import sales_invoice_create


class CustomerSerializer(serializers.ModelSerializer):
    total_purchases = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ["id", "name", "phone", "city", "status", "total_purchases"]
        read_only_fields = ["id"]

    def get_total_purchases(self, obj) -> int:
        # List endpoint annotates this (see selectors.customer_list) to
        # avoid an N+1 query; fall back to the property for a single object
        # fetched without the annotation (e.g. after a plain .get()).
        annotated = getattr(obj, "total_purchases_annotated", None)
        return annotated if annotated is not None else obj.total_purchases


class InvoiceLineItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source="item.name", read_only=True)
    subtotal = serializers.DecimalField(max_digits=14, decimal_places=0, read_only=True)

    class Meta:
        model = InvoiceLineItem
        fields = ["id", "item", "item_name", "quantity", "unit_price", "subtotal"]


class InvoiceSerializer(serializers.ModelSerializer):
    """Read serializer — nested line items and the computed total."""

    customer_name = serializers.CharField(source="customer.name", read_only=True)
    amount = serializers.DecimalField(max_digits=14, decimal_places=0, read_only=True)
    line_items = InvoiceLineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id", "invoice_number", "customer", "customer_name",
            "date", "status", "amount", "line_items",
        ]
        read_only_fields = ["id", "invoice_number"]


class InvoiceLineItemInputSerializer(serializers.Serializer):
    item = serializers.PrimaryKeyRelatedField(queryset=InventoryItem.objects.all())
    quantity = serializers.IntegerField(min_value=1)
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=0, min_value=0)


class InvoiceCreateSerializer(serializers.Serializer):
    """Write serializer for POST /sales/invoices/ — the 'ثبت فروش' form.
    Deliberately a plain Serializer, not a ModelSerializer: creating an
    invoice is a multi-step operation (line items + stock issue), which
    belongs in services.sales_invoice_create, not in a serializer's
    .create(). This just validates shape and hands off."""

    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    date = serializers.DateField()
    line_items = InvoiceLineItemInputSerializer(many=True, allow_empty=False)

    def save(self, **kwargs):
        return sales_invoice_create(actor=self.context["request"].user, **self.validated_data)
