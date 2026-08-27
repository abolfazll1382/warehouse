from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from apps.hr import selectors
from apps.hr.permissions import IsHRStaff
from apps.hr.serializers import EmployeeSerializer, PayrollSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRStaff]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["department", "status"]
    search_fields = ["full_name", "position"]

    def get_queryset(self):
        return selectors.employee_list(
            department=self.request.query_params.get("department"),
            status=self.request.query_params.get("status"),
        )


class PayrollViewSet(viewsets.ModelViewSet):
    serializer_class = PayrollSerializer
    permission_classes = [IsHRStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["employee", "status", "period"]

    def get_queryset(self):
        return selectors.payroll_list(employee_id=self.request.query_params.get("employee"))
