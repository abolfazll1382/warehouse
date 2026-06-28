# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/views/reorder_suggestion.py

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.db import models

from inventory.models import Inventory
from inventory.serializers.reorder_suggestion import (
    ReorderSuggestionSerializer,
)

from users.permissions import StrictModelPermissions

class ReorderSuggestionListView(
    ListAPIView
):

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]

    serializer_class = (
        ReorderSuggestionSerializer
    )

    def list(
        self,
        request,
        *args,
        **kwargs,
    ):
        suggestions = []

        inventories = (
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

        for inventory in inventories:

            deficit = (
                inventory.minimum_quantity
                - inventory.quantity
            )

            suggested_order = (
                deficit * 2
            )

            suggestions.append(
                {
                    "inventory_id": inventory.id,
                    "warehouse": inventory.warehouse.name,
                    "product": inventory.product.name,
                    "current_quantity": inventory.quantity,
                    "minimum_quantity": inventory.minimum_quantity,
                    "suggested_order_quantity": suggested_order,
                }
            )

        serializer = (
            self.get_serializer(
                suggestions,
                many=True,
            )
        )

        return Response(
            serializer.data
        )