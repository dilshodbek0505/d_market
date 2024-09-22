from django.contrib import admin
from apps.users.models import User, Address
from django.contrib.auth.admin import UserAdmin
from django.utils.text import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = [
        (_('Main'), {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'phone_number', 'coins')}),
        (_('Permissions'), {'fields': ('groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    list_display = ('username', 'full_name', 'phone_number')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ...