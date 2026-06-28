# MY_DJANGO PROJECTS TRAINING/warehouse_erp/inventory/urls.py

from django.urls import path

from rest_framework.routers import DefaultRouter

from inventory.views.stock_movement import (
    StockMovementViewSet,
)

from inventory.views.low_stock import (
    LowStockListView,
)

from inventory.views.reorder_suggestion import (
    ReorderSuggestionListView,
)

router = DefaultRouter()

router.register(
    "stock-movements",
    StockMovementViewSet,
    basename="stock-movements",
)

urlpatterns = [
    *router.urls,

    path(
        "low-stock/",
        LowStockListView.as_view(),
        name="low-stock",
    ),

    path(
        "reorder-suggestions/",
        ReorderSuggestionListView.as_view(),
        name="reorder-suggestions",
    ),
]