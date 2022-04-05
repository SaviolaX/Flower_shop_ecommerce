from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile
from .forms import *


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationsForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['email', 'first_name', 'last_name']
    
    # Django admin content hierarchy
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
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
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )