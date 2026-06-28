# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/views/low_stock.py

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django.db import models

from inventory.models import Inventory
from inventory.serializers.low_stock import (
    LowStockSerializer,
)

from users.permissions import StrictModelPermissions


class LowStockListView(
    ListAPIView
):

    serializer_class = (
        LowStockSerializer
    )

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]

    def get_queryset(
        self,
    ):
        return (
            Inventory.objects
            .filter(
                quantity__lte=models.F(
                    "minimum_quantity"
                )
            )
            .select_related(
                "warehouse",
                "product",
            )
        )