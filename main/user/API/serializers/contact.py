from user.models import AppUser, UserContacts
from rest_framework import serializers

"""
Serializers in this file will be used to retrieve user profile data
"""

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ["username", "email", "bio", "first_name", "last_name"]
        
class ContactAssociationSerializer(serializers.ModelSerializer):
    user1 = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")
    user2 = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")
    
    class Meta:
        model = UserContacts
        fields = ["user1", "user2", "contacts_since", "request_accepted"]