# import api stuff
from rest_framework.views import APIView

# import models
from user.models import AppUser
from conversation.models import PrivateConversation

# http imports
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# serializers imports
from conversation.API.serializers.privateConversationSerializer import PrivateConversationSerializer

# authentications imports
from rest_framework.authentication import TokenAuthentication

# permissions imports
from rest_framework.permissions import IsAuthenticated

# other libs
from datetime import datetime

class PrivateConversationView(APIView):
    """
    This method will create an instance of PrivateConversation between 2 registered users.
    Then it will create the first Message instance in this PrivateConversation.
    It is triggered when the user writes a message to one of it's contacts.
    If the sender blacklisted the receiver or vice-versa they cannot send messages to each other
    until the blacklisting is removed
    """
    
    def post(self, request, format=None):
        """Create a new conversation instance"""
        try:
            # search the two users in db first
            user1 = request.user
            user2 = AppUser.objects.get(username="aallisonjj")
            print(user1, type(user1))
            print(user2, type(user2))
            # search if previos private conversation between the 2 users
            test_query_1 = PrivateConversation.objects.filter(user1=user1, user2=user2).count()
            test_query_2 = PrivateConversation.objects.filter(user1=user2, user2=user1).count()
            
            if (test_query_1==0 and test_query_2==0):
                # if no previous conversation entry between the two users
                # attempt to create new conversation
                try:
                    serializer = PrivateConversationSerializer(data={"user1": user1, "user2": user2, "creation_date": datetime.now(), "conversation_flag":False})
                    print("serializer processed")
                    
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    print("serializer valid")
                    # return serializer.data
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                    # if serializer.is_valid():
                    #     print("serializer valid")
                    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
                    # else:
                    #     return Response({"message":"Serializer not valid"})
                        
                except:
                    print("2nd try exception")
                    # user does not exist
                    return Response({"message":"Request could not be processed on creation"})
            
            
        except e:
            print("1st try exception")
            return Response({"message":"Users not found"})
            
        return Response({"message": "Request could not be processed"}, status=status.HTTP_400_BAD_REQUEST)