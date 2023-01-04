from user.models import AppUser
from rest_framework import serializers

"""
Serializers in this file will be used to add, retrieve and change user profile data
"""

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ["username", "email", "bio", "first_name", "last_name"]
        
