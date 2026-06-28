from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from warehouses.models import Warehouse
from warehouses.serializers import WarehouseSerializer

from users.permissions import StrictModelPermissions

class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.select_related('manager').all().order_by('-created_at')
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated, StrictModelPermissions]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active', 'manager']
    search_fields = ['name', 'code', 'address']

    def get_queryset(self):
        # 1. If the user is the CEO, they see ALL warehouses
        if self.request.user.groups.filter(name="CEO").exists():
            return Warehouse.objects.all()
            
        # 2. For everyone else, they only see the warehouses ticked on their profile!
        employee_profile = self.request.user.employee_profile
        return employee_profile.accessible_warehouses.all()