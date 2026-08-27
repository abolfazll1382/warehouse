from rest_framework import serializers

from apps.inventory.models import Category, InventoryItem, StockMovement


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class InventoryItemSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = InventoryItem
        fields = [
            "id", "sku", "name", "category", "category_name",
            "quantity", "unit", "reorder_threshold", "status",
        ]
        read_only_fields = ["id", "quantity"]  # quantity only changes via receive/issue actions


class StockMovementSerializer(serializers.ModelSerializer):
    actor_name = serializers.CharField(source="actor.full_name", read_only=True, default=None)

    class Meta:
        model = StockMovement
        fields = ["id", "item", "quantity", "reason", "reference", "note", "actor", "actor_name", "created_at"]
        read_only_fields = ["id", "actor", "created_at"]


class StockReceiveSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    reason = serializers.ChoiceField(choices=StockMovement.Reason.choices, default=StockMovement.Reason.PURCHASE)
    reference = serializers.CharField(max_length=64, required=False, allow_blank=True)
    note = serializers.CharField(max_length=255, required=False, allow_blank=True)


class StockIssueSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    reason = serializers.ChoiceField(choices=StockMovement.Reason.choices, default=StockMovement.Reason.SALE)
    reference = serializers.CharField(max_length=64, required=False, allow_blank=True)
    note = serializers.CharField(max_length=255, required=False, allow_blank=True)
