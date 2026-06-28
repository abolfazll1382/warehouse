# MY_DJANGO PROJECTS TRAINING/warehouse_erp/dashboard/serializers/dashboard.py

from rest_framework import serializers


class DashboardSerializer(
    serializers.Serializer
):

    products = serializers.IntegerField()

    warehouses = serializers.IntegerField()

    suppliers = serializers.IntegerField()

    employees = serializers.IntegerField()

    low_stock_items = serializers.IntegerField()

    draft_purchase_orders = serializers.IntegerField()

    approved_purchase_orders = serializers.IntegerField()

    received_purchase_orders = serializers.IntegerField()