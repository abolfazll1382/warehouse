# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/serializers/reorder_suggestion.py

from rest_framework import serializers


class ReorderSuggestionSerializer(
    serializers.Serializer
):

    inventory_id = serializers.IntegerField()

    warehouse = serializers.CharField()

    product = serializers.CharField()

    current_quantity = serializers.IntegerField()

    minimum_quantity = serializers.IntegerField()

    suggested_order_quantity = serializers.IntegerField()