# sales/serializers.py

from rest_framework import serializers
from sales.models import SalesOrder, SalesOrderItem

class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = ('id', 'product', 'quantity', 'unit_price')

class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True)
    customer_name = serializers.CharField(source='customer.company_name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)

    class Meta:
        model = SalesOrder
        fields = (
            'id', 'customer', 'customer_name', 'warehouse', 'warehouse_name', 
            'status', 'processed_by', 'notes', 'items', 'created_at'
        )
        read_only_fields = ('status', 'processed_by', 'created_at')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sales_order = SalesOrder.objects.create(**validated_data)
        
        for item_data in items_data:
            SalesOrderItem.objects.create(sales_order=sales_order, **item_data)
            
        return sales_order