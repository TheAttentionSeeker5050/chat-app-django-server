"""
Serializer for create private conversation and first private conversation message object
"""

# serializer methods imports
from rest_framework import serializers

# models and serializers imports 
from user.models import AppUser
from conversation.models import PrivateConversation

# other imports
from datetime import datetime

# field validators


# your serializers go here
class PrivateConversationSerializer(serializers.ModelSerializer):
    # user1 = serializers.SlugRelatedField(
    #     slug_field="username", 
    #     queryset=AppUser.objects.all())
    # user2 = serializers.SlugRelatedField(
    #     slug_field="username",
    #     queryset=AppUser.objects.all())
    
    class Meta:
        model = PrivateConversation
        fields = ["user1", "user2", "creation_date"]
        
    
    

