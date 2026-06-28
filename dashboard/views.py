# MY_DJANGO PROJECTS TRAINING/warehouse_erp/dashboard/views/dashboard.py

from django.db.models import F

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Product
from warehouses.models import Warehouse
from purchasing.models import (
    Supplier,
    PurchaseOrder,
)
from users.models import EmployeeProfile
from inventory.models import Inventory

from .serializers import (
    DashboardSerializer,
)

from users.permissions import IsCEO


class DashboardView(GenericAPIView):

    serializer_class = (
        DashboardSerializer
    )

    permission_classes = [
        IsAuthenticated,
        IsCEO
    ]

    def get(
        self,
        request,
        *args,
        **kwargs,
    ):

        data = {
            "products":
                Product.objects.count(),

            "warehouses":
                Warehouse.objects.count(),

            "suppliers":
                Supplier.objects.count(),

            "employees":
                EmployeeProfile.objects.count(),

            "low_stock_items":
                Inventory.objects.filter(
                    quantity__lte=F(
                        "minimum_quantity"
                    )
                ).count(),

            "draft_purchase_orders":
                PurchaseOrder.objects.filter(
                    status="DRAFT"
                ).count(),

            "approved_purchase_orders":
                PurchaseOrder.objects.filter(
                    status="APPROVED"
                ).count(),

            "received_purchase_orders":
                PurchaseOrder.objects.filter(
                    status="RECEIVED"
                ).count(),
        }

        serializer = (
            self.get_serializer(
                data
            )
        )

        return Response(
            serializer.data
        )