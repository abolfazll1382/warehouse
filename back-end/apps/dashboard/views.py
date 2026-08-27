from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboard import selectors
from apps.dashboard.serializers import (
    KpiSerializer,
    MonthlyPointSerializer,
    OverviewSerializer,
    TopProductSerializer,
    TransactionSerializer,
)


class OverviewView(APIView):
    """
    GET /api/v1/dashboard/overview/

    Everything the Overview page needs in one round trip: KPIs, the
    7-month sales/orders trend, recent transactions and top products.
    Any authenticated user can view it — it's read-only and cross-department
    by nature, unlike the department-gated module endpoints.
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(responses=OverviewSerializer)
    def get(self, request):
        return Response(
            {
                "kpis": KpiSerializer(selectors.kpi_summary()["kpis"], many=True).data,
                "monthly_trend": MonthlyPointSerializer(selectors.monthly_trend(), many=True).data,
                "recent_transactions": TransactionSerializer(selectors.recent_transactions(), many=True).data,
                "top_products": TopProductSerializer(selectors.top_products(), many=True).data,
            }
        )
