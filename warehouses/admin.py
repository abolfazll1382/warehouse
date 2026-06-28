# MY_DJANGO PROJECTS TRAINING/warehouse_erp/warehouses/admin.py

from django.contrib import admin

from warehouses.models import Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "name",
        "manager",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )