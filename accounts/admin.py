from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'first_name', 'last_name', 'age',  ]
    ordering = ('-date_joined',)

    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields': ('age', ), }),
    )

    fieldsets = UserAdmin.fieldsets+(
        (None, {'fields': ('age', ), }),
    )
