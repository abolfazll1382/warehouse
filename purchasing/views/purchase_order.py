# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/views/purchase_order.py

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django.core.exceptions import ValidationError

from purchasing.services.receive import receive_purchase_order
from purchasing.serializers.purchase_order import PurchaseOrder, PurchaseOrderSerializer
from purchasing.services.approve import (
    approve_purchase_order,
)

from users.permissions import (
    CanApprovePurchaseOrder,
    CanManagePurchaseOrder,
    CanReceivePurchaseOrder,
    StrictModelPermissions,
)


class PurchaseOrderViewSet(ModelViewSet):

    queryset = PurchaseOrder.objects.all().order_by("-id")
    serializer_class = PurchaseOrderSerializer

    permission_classes = [IsAuthenticated, StrictModelPermissions]

    def get_permissions(self):
        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), StrictModelPermissions(), CanManagePurchaseOrder()]

        if self.action == "approve":
            return [IsAuthenticated(), StrictModelPermissions(), CanApprovePurchaseOrder()]

        if self.action == "receive":
            return [IsAuthenticated(), StrictModelPermissions(), CanReceivePurchaseOrder()]

        # For GET requests (list and retrieve)
        return [IsAuthenticated(), StrictModelPermissions()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=["post"])
    def receive(self, request, pk=None):

        purchase_order = self.get_object()

        warehouse_id = request.data.get("warehouse")

        if not warehouse_id:
            return Response(
                {"error": "warehouse is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            receive_purchase_order(
                purchase_order=purchase_order,
                warehouse_id=warehouse_id,
                performed_by=request.user,
            )

        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Purchase Order received successfully"},
            status=status.HTTP_200_OK
        )
    
    @action(
        detail=True,
        methods=["post"],
    )
    def approve(
        self,
        request,
        pk=None,
    ):
        
        purchase_order = (
            self.get_object()
        )

        try:
            approve_purchase_order(
                purchase_order=purchase_order
        )

        except Exception as e:
            return Response(
                {
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message":
                "Purchase Order approved successfully"
            }
        )