from django.contrib import admin

from apps.purchasing.models import PurchaseOrder, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "contact", "rating", "status"]
    list_filter = ["status", "category"]
    search_fields = ["name"]


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "supplier", "date", "amount", "status"]
    list_filter = ["status"]
    autocomplete_fields = ["supplier"]
    readonly_fields = ["order_number"]
