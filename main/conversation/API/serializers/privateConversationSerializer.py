"""
Serializer for create private conversation and first private conversation message object
"""

# serializer methods imports
from user.models import AppUser
from rest_framework import serializers
from user.API.serializers.userProfile import UserProfileSerializer
from .messageSerializer import MessageOverPrivateConversationSerializer

# other imports
from datetime import datetime

# field validators


# your serializers go here
class PrivateConversationSerializer():
    first_message = MessageOverPrivateConversationSerializer()
    user_1_id = UserProfileSerializer(required=True)
    user_2_id = UserProfileSerializer(required=True)
    creation_date = serializers.DateField(default=datetime.now())
    

