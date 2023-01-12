from user.models import AppUser, ContactBook
from rest_framework import serializers

"""
Serializers in this file will be used to add, retrieve and change user profile and contact data
"""

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializers for returning contact data from GET request
    """
    class Meta:
        model = AppUser
        fields = ["username", "email", "bio", "first_name", "last_name"]
        
class ContactBookSerializer(serializers.ModelSerializer):
    """
    Serializers of the contact book associations
    """
    user1 = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    user2 = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    
    class Meta:
        model = ContactBook
        fields = ["user1", "user2"]