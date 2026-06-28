# sales/urls.py

from rest_framework.routers import DefaultRouter
from sales.views import SalesOrderViewSet

router = DefaultRouter()
router.register('sales-orders', SalesOrderViewSet, basename='sales-orders')

urlpatterns = router.urls