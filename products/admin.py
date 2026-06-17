from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sku",
        "name",
        "unit",
        "minimum_stock",
        "is_active",
    )

    search_fields = (
        "sku",
        "name",
        "barcode",
    )

    list_filter = (
        "is_active",
        "unit",
    )