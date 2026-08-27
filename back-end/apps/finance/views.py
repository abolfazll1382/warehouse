from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.finance import selectors
from apps.finance.permissions import IsFinanceStaff
from apps.finance.serializers import AccountSerializer, FinanceRecordSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsFinanceStaff]

    def get_queryset(self):
        return selectors.account_list()


class FinanceRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinanceRecordSerializer
    permission_classes = [IsFinanceStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type", "account", "category"]

    def get_queryset(self):
        return selectors.finance_record_list(
            type=self.request.query_params.get("type"),
            account_id=self.request.query_params.get("account"),
        )
