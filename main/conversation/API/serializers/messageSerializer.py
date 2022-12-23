
"""This serializer will create messages"""

# serializer methods imports
from user.models import AppUser
from rest_framework import serializers
from user.API.serializers.userProfile import UserProfileSerializer
from conversation.models import ChatMessage

# other imports
from datetime import datetime

class MessageOverGroupConversationSerializer():
    pass

class MessageOverPrivateConversationSerializer(serializers.ModelSerializer):
    
    class Meta:
        """I use the meta class of the model serializer to write less code on this one"""
        model = ChatMessage
        fields = [
            "user_id",
            "message_type",
            "message_text",
            "creation_date",
            "edition_date",
            "private_conversation_id",
        ]
        
    