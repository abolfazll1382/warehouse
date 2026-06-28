# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/serializers/low_stock.py

from rest_framework import serializers

from inventory.models import Inventory


class LowStockSerializer(
    serializers.ModelSerializer
):

    warehouse = serializers.CharField(
        source="warehouse.name",
        read_only=True,
    )

    product = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    class Meta:
        model = Inventory

        fields = (
            "id",
            "warehouse",
            "product",
            "quantity",
            "minimum_quantity",
        )