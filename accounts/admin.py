from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields': ('age', ), }),
    )

    fieldsets = UserAdmin.fieldsets+(
        (None, {'fields': ('age', ), }),
    )
