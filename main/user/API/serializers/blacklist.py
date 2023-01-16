from user.models import AppUser, ContactsBlacklist
from rest_framework import serializers
from user.API.serializers.userProfile import UserProfileSerializer
"""
Serializers in this file will be used to retrieve and change user blacklist data
"""

class BlacklistSerializer(serializers.ModelSerializer):
    user1 = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")
    user2 = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")
    
    class Meta:
        model = AppUser
        fields = ["user1", "user2"]
        

    
    