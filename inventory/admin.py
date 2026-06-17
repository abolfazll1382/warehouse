from django.contrib import admin

from inventory.models import Inventory, StockMovement


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "warehouse",
        "product",
        "quantity",
    )

    search_fields = (
        "warehouse__name",
        "product__name",
        "product__sku",
    )

    list_filter = (
        "warehouse",
    )


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "inventory",
        "movement_type",
        "quantity",
        "performed_by",
        "created_at",
    )

    list_filter = (
        "movement_type",
        "created_at",
    )

    search_fields = (
        "inventory__product__name",
        "inventory__product__sku",
        "performed_by__username",
    )