from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms.models import Room


class UserInline(admin.TabularInline):
    model = Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    inlines = (UserInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
