from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser,  ContactsBlacklist, ContactBook

admin.site.register(AppUser, UserAdmin)
admin.site.register(ContactsBlacklist)
admin.site.register(ContactBook)

