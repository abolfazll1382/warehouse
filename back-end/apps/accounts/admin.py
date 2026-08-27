from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ["email"]
    list_display = ["email", "first_name", "last_name", "department", "is_staff", "is_active"]
    list_filter = ["department", "is_staff", "is_active"]
    search_fields = ["email", "first_name", "last_name"]

    # AbstractUser's fieldsets reference `username`, which we removed —
    # redeclare them around email + our custom fields instead.
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number")}),
        ("Work", {"fields": ("department",)}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "department", "password1", "password2"),
            },
        ),
    )
