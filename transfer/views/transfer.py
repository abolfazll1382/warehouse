# MY_DJANGO PROJECTS TRAINING/warehouse_erp/transfer/views/transfer.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from transfer.models import Transfer
from transfer.serializers.transfer import (
    TransferListSerializer,
    TransferCreateSerializer,
)

from users.permissions import IsCEO, StrictModelPermissions

class TransferViewSet(ModelViewSet):

    queryset = Transfer.objects.all().order_by("-id")

    permission_classes = [
        IsAuthenticated,
        IsCEO,
        StrictModelPermissions
    ]
    
    def get_serializer_class(self):

        if self.action == "create":
            return TransferCreateSerializer

        return TransferListSerializer

    def perform_create(self, serializer):

        serializer.save(
            performed_by=self.request.user,
        )