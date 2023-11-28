"""Admin site settings of the 'Users' application."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Settings for presenting 'User' model on the admin site."""

    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    exclude = ("username",)
    search_fields = ("email",)
    list_filter = ("email",)
    ordering = ("email",)

    readonly_fields = ("date_joined",)
    search_fields = (
        "username",
        "email",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.unregister(Group)
