from django.contrib import admin

from apps.inventory.models import Category, InventoryItem, StockMovement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 0
    readonly_fields = ["quantity", "reason", "reference", "actor", "created_at"]
    can_delete = False


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ["sku", "name", "category", "quantity", "unit", "status"]
    list_filter = ["category"]
    search_fields = ["sku", "name"]
    inlines = [StockMovementInline]


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ["item", "quantity", "reason", "reference", "actor", "created_at"]
    list_filter = ["reason"]
    readonly_fields = ["created_at", "updated_at"]
