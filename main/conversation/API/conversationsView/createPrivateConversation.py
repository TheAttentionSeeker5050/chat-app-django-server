"""
This method will create an instance of PrivateConversation between 2 registered users.
Then it will create the first Message instance in this PrivateConversation.
It is triggered when the user writes a message to one of it's contacts
"""

# import api stuff
from rest_framework.views import APIView
from rest_framework.response import Response

# import models
from user.models import AppUser

class 