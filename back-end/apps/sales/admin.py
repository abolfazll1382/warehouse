from django.contrib import admin

from apps.sales.models import Customer, Invoice, InvoiceLineItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "city", "status"]
    list_filter = ["status", "city"]
    search_fields = ["name", "phone"]


class InvoiceLineItemInline(admin.TabularInline):
    model = InvoiceLineItem
    extra = 1
    autocomplete_fields = ["item"]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["invoice_number", "customer", "date", "amount", "status"]
    list_filter = ["status"]
    readonly_fields = ["invoice_number"]
    autocomplete_fields = ["customer"]
    inlines = [InvoiceLineItemInline]
