from rest_framework import serializers
from warehouses.models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    # This ensures we get the manager's username instead of just their ID in the API response
    manager_username = serializers.CharField(source='manager.username', read_only=True)

    class Meta:
        model = Warehouse
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')