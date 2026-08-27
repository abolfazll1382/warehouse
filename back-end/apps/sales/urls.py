from rest_framework.routers import DefaultRouter

from apps.sales.views import CustomerViewSet, InvoiceViewSet

app_name = "sales"

router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customer")
router.register("invoices", InvoiceViewSet, basename="invoice")

urlpatterns = router.urls
