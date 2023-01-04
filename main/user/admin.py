from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser,  ContactsBlacklist

admin.site.register(AppUser, UserAdmin)
admin.site.register(ContactsBlacklist)

