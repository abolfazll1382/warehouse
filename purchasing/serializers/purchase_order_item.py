# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/serializers/purchase_order_item.py

from rest_framework import serializers

from purchasing.models import PurchaseOrderItem


class PurchaseOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrderItem

        fields = (
            "id",
            "product",
            "quantity",
            "unit_price",
        )