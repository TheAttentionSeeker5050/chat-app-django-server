"""
I am working on this, will get it done soon
"""

from rest_framework import permissions

# import models
from user.models import AppUser, ContactsBlacklist

class UserNotBlacklistedPermission(permissions.BasePermission):
    """Return false if there is a blacklist between 2 users, or true if not"""
    
    def has_object_permission(self, request, view, obj):
        try:
            # first lookup for 2 users
            user1 = AppUser.objects.get(username=request.user)
            user2 = obj
        except e:
            """Nothing happens"""