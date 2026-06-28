# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/urls.py

from rest_framework.routers import DefaultRouter

from purchasing.views.purchase_order import PurchaseOrderViewSet


router = DefaultRouter()

router.register(
    "purchase-orders",
    PurchaseOrderViewSet,
    basename="purchase-orders",
)

urlpatterns = router.urls