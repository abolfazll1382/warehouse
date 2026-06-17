from rest_framework.viewsets import ModelViewSet

from transfer.models import Transfer
from transfer.serializers.transfer import (
    TransferListSerializer,
    TransferCreateSerializer,
)


class TransferViewSet(ModelViewSet):

    queryset = Transfer.objects.all().order_by("-id")

    def get_serializer_class(self):

        if self.action == "create":
            return TransferCreateSerializer

        return TransferListSerializer

    def perform_create(self, serializer):

        serializer.save(
            performed_by=self.request.user,
        )