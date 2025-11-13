from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreation, CustomUserchangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserchangeForm
    model = CustomUser

    # Fields displayed in the list view
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
        "is_superuser",
        "is_active",
    ]

    # Fields used in the edit view
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields used in the add view
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ("email", "username", "name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
