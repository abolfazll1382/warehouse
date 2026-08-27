from django.contrib import admin

from apps.hr.models import Employee, Payroll


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position", "department", "hire_date", "status"]
    list_filter = ["department", "status"]
    search_fields = ["full_name", "position"]


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ["employee", "period", "base_salary", "net_pay", "status"]
    list_filter = ["status"]
    autocomplete_fields = ["employee"]
