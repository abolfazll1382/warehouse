# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/serializers/stock_movement.py

from rest_framework import serializers

from inventory.models import StockMovement


class StockMovementSerializer(
    serializers.ModelSerializer
):

    warehouse = serializers.CharField(
        source="inventory.warehouse.name",
        read_only=True,
    )

    product = serializers.CharField(
        source="inventory.product.name",
        read_only=True,
    )

    performed_by_username = serializers.CharField(
        source="performed_by.username",
        read_only=True,
    )

    class Meta:
        model = StockMovement

        fields = (
            "id",
            "warehouse",
            "product",
            "movement_type",
            "quantity",
            "performed_by_username",
            "notes",
            "created_at",
        )

        read_only_fields = fields