from rest_framework.routers import DefaultRouter

from apps.production.views import ProductionLineViewSet, QualityCheckViewSet

app_name = "production"

router = DefaultRouter()
router.register("lines", ProductionLineViewSet, basename="production-line")
router.register("quality-checks", QualityCheckViewSet, basename="quality-check")

urlpatterns = router.urls
