from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from apps.production import selectors
from apps.production.permissions import IsProductionStaffOrReadOnly
from apps.production.serializers import ProductionLineSerializer, QualityCheckSerializer


class ProductionLineViewSet(viewsets.ModelViewSet):
    serializer_class = ProductionLineSerializer
    permission_classes = [IsProductionStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    search_fields = ["name", "product"]

    def get_queryset(self):
        return selectors.production_line_list()


class QualityCheckViewSet(viewsets.ModelViewSet):
    serializer_class = QualityCheckSerializer
    permission_classes = [IsProductionStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["line", "result"]
    search_fields = ["product"]

    def get_queryset(self):
        return selectors.quality_check_list(
            line_id=self.request.query_params.get("line"),
            result=self.request.query_params.get("result"),
        )
