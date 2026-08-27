from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from apps.purchasing import selectors
from apps.purchasing.permissions import IsPurchasingStaffOrReadOnly
from apps.purchasing.serializers import PurchaseOrderSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsPurchasingStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status", "category"]
    search_fields = ["name"]

    def get_queryset(self):
        return selectors.supplier_list(status=self.request.query_params.get("status"))


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsPurchasingStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["supplier", "status"]

    def get_queryset(self):
        return selectors.purchase_order_list(
            supplier_id=self.request.query_params.get("supplier"),
            status=self.request.query_params.get("status"),
        )
