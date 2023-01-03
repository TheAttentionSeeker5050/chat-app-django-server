# import serializer
from user.API.serializers.contact import ContactSerializer, ContactAssociationSerializer
from rest_framework.views import APIView

# import models
from user.models import AppUser, UserContacts

# http imports
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# authentications
from rest_framework.authentication import TokenAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated

# other libs
from datetime import datetime

class SendContactInvitationAPIView(APIView):
    """
    This api endpoint will send an invitation to an existing non contact user
    this will be necessary for enabling permissions on the platform
    """
    
    def post(self, request, contact_username, format=None):
        """post the invitation on the database with a status accepted equals to false"""
        try:
            # find users first
            user1 = AppUser.objects.get(username=request.user)
            user2 = AppUser.objects.get(username=contact_username)
        
            # check if there are any previous contacts association with user pair
            test_case_query1 = UserContacts.objects.filter(user1=user1, user2=user2).count()
            test_case_query2 = UserContacts.objects.filter(user1=user2, user2=user1).count()
            
            if test_case_query1 == 0 and test_case_query2 == 0:
                # in case empty, create new contact request
                
                try:
                    query = UserContacts.objects.create(user1=user1, user2=user2, contacts_since=datetime.now(), request_accepted=False)
                    query.save()
                    return Response({"message":"Send Contact Request Successful"},status=status.HTTP_201_CREATED)
                except e:
                    # in case it could not be created
                    return Response({"message":"Send Contact Request Unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message":"Contact is already added"}, status=status.HTTP_400_BAD_REQUEST)
            
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message":"Could not create contact association"}, status=status.HTTP_204_NO_CONTENT)