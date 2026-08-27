from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.inventory import selectors, services
from apps.inventory.models import Category, InventoryItem, StockMovement
from apps.inventory.permissions import IsWarehouseStaffOrReadOnly
from apps.inventory.serializers import (
    CategorySerializer,
    InventoryItemSerializer,
    StockIssueSerializer,
    StockMovementSerializer,
    StockReceiveSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsWarehouseStaffOrReadOnly]


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsWarehouseStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["sku", "name"]
    ordering_fields = ["name", "quantity"]

    def get_queryset(self):
        return selectors.inventory_item_list(category_id=self.request.query_params.get("category"))

    @action(detail=True, methods=["post"])
    def receive(self, request, pk=None):
        """POST /inventory/items/{id}/receive/ — add stock to the warehouse."""
        item = self.get_object()
        serializer = StockReceiveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.inventory_item_receive(item=item, actor=request.user, **serializer.validated_data)
        return Response(InventoryItemSerializer(item).data)

    @action(detail=True, methods=["post"])
    def issue(self, request, pk=None):
        """POST /inventory/items/{id}/issue/ — remove stock from the warehouse."""
        item = self.get_object()
        serializer = StockIssueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.inventory_item_issue(item=item, actor=request.user, **serializer.validated_data)
        return Response(InventoryItemSerializer(item).data)


class StockMovementViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only — movements are only ever created via the receive/issue
    actions above, never directly, so there's no create/update/delete here."""

    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["item", "reason"]

    def get_queryset(self):
        return selectors.stock_movement_list(item_id=self.request.query_params.get("item"))
