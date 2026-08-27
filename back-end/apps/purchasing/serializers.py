from rest_framework import serializers

from apps.purchasing.models import PurchaseOrder, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "category", "contact", "rating", "status"]
        read_only_fields = ["id"]


class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ["id", "order_number", "supplier", "supplier_name", "date", "amount", "status"]
        read_only_fields = ["id", "order_number"]
