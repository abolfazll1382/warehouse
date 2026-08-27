from rest_framework.routers import DefaultRouter

from apps.inventory.views import CategoryViewSet, InventoryItemViewSet, StockMovementViewSet

app_name = "inventory"

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("items", InventoryItemViewSet, basename="inventory-item")
router.register("movements", StockMovementViewSet, basename="stock-movement")

urlpatterns = router.urls
