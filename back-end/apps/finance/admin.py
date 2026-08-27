from django.contrib import admin

from apps.finance.models import Account, FinanceRecord


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["name", "account_type", "balance"]
    list_filter = ["account_type"]
    search_fields = ["name"]


@admin.register(FinanceRecord)
class FinanceRecordAdmin(admin.ModelAdmin):
    list_display = ["description", "type", "category", "amount", "date", "account"]
    list_filter = ["type", "category"]
    search_fields = ["description"]
    autocomplete_fields = ["account"]
