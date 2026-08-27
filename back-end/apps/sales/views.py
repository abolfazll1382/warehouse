from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response

from apps.sales import selectors
from apps.sales.permissions import IsSalesStaffOrReadOnly
from apps.sales.serializers import CustomerSerializer, InvoiceCreateSerializer, InvoiceSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsSalesStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status", "city"]
    search_fields = ["name", "phone"]

    def get_queryset(self):
        return selectors.customer_list(status=self.request.query_params.get("status"))


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSalesStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["customer", "status"]

    def get_queryset(self):
        return selectors.invoice_list(
            customer_id=self.request.query_params.get("customer"),
            status=self.request.query_params.get("status"),
        )

    def get_serializer_class(self):
        # Reading an invoice returns nested line items + computed amount;
        # writing one is the multi-step service call — different shapes,
        # different serializers, instead of one serializer trying to do both.
        if self.action == "create":
            return InvoiceCreateSerializer
        return InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice = serializer.save()
        return Response(InvoiceSerializer(invoice).data, status=201)
