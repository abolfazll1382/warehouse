from rest_framework.routers import DefaultRouter

from apps.purchasing.views import PurchaseOrderViewSet, SupplierViewSet

app_name = "purchasing"

router = DefaultRouter()
router.register("suppliers", SupplierViewSet, basename="supplier")
router.register("orders", PurchaseOrderViewSet, basename="purchase-order")

urlpatterns = router.urls
