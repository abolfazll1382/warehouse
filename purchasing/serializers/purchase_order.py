# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/serializers/purchase_order.py

from rest_framework import serializers

from purchasing.models import PurchaseOrder, PurchaseOrderItem

from purchasing.serializers.purchase_order_item import (
    PurchaseOrderItemSerializer,
)


class PurchaseOrderSerializer(serializers.ModelSerializer):

    items = PurchaseOrderItemSerializer(
        many=True,
        required=False,
    )

    class Meta:
        model = PurchaseOrder

        fields = (
            "id",
            "supplier",
            "status",
            "created_by",
            "created_at",
            "items",
        )

        read_only_fields = (
            "status",
            "created_by",
            "created_at",
        )

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])

        purchase_order = PurchaseOrder.objects.create(
            **validated_data
        )

        for item_data in items_data:
            PurchaseOrderItem.objects.create(
                purchase_order=purchase_order,
                **item_data
            )

        return purchase_order