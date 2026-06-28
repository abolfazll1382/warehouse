from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend

from inventory.models import StockMovement
from inventory.serializers.stock_movement import StockMovementSerializer

from users.permissions import StrictModelPermissions

class StockMovementViewSet(ReadOnlyModelViewSet):
    queryset = (
        StockMovement.objects
        .select_related("inventory__warehouse", "inventory__product", "performed_by")
        .order_by("-created_at")
    )
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated, StrictModelPermissions]

    # --- NEW: Powerful Searching and Filtering ---
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Exact match filters (e.g., /api/stock-movements/?movement_type=PURCHASE)
    filterset_fields = ['movement_type', 'inventory__warehouse', 'inventory__product']
    
    # Text search (e.g., /api/stock-movements/?search=Laptop)
    search_fields = ['notes', 'inventory__product__name', 'performed_by__username']
    
    # Allow user to sort (e.g., /api/stock-movements/?ordering=quantity)
    ordering_fields = ['created_at', 'quantity']