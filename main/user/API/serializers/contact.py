from user.models import AppUser
from rest_framework import serializers

"""
Serializers in this file will be used to retrieve user profile data
"""

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ["username", "email", "bio", "phone_number", "first_name", "last_name"]
        
        