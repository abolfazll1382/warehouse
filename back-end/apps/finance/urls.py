from rest_framework.routers import DefaultRouter

from apps.finance.views import AccountViewSet, FinanceRecordViewSet

app_name = "finance"

router = DefaultRouter()
router.register("accounts", AccountViewSet, basename="account")
router.register("records", FinanceRecordViewSet, basename="finance-record")

urlpatterns = router.urls
