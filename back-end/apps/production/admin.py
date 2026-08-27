from django.contrib import admin

from apps.production.models import ProductionLine, QualityCheck


@admin.register(ProductionLine)
class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ["name", "product", "capacity", "efficiency", "status"]
    list_filter = ["status"]
    search_fields = ["name", "product"]


@admin.register(QualityCheck)
class QualityCheckAdmin(admin.ModelAdmin):
    list_display = ["product", "date", "inspector", "result"]
    list_filter = ["result"]
    search_fields = ["product"]
    autocomplete_fields = ["inspector", "line"]
