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

class ContactInvitation(APIView):
    """
    This api endpoint will send an invitation to an existing non contact user
    this will be necessary for enabling permissions on the platform
    """
    
    def put(self, request, contact_username, format=None):
        """accept the invitation to contact"""
        try:
            # find users first
            user1 = AppUser.objects.get(username=contact_username) # users are switched from the sendContactInvitation.py because 
            # we are accepting their request
            user2 = AppUser.objects.get(username=request.user)
        
            # check if there are any previous contacts association with user pair
            test_case_query = UserContacts.objects.filter(user1=user1, user2=user2).count()
            
            if test_case_query > 0:
                # in case it is not empty, update contact request
                
                try:
                    query = UserContacts.objects.get(user1=user1, user2=user2)
                    query.request_accepted = True
                    query.save()
                    return Response({"message":"Accept Invite Successful"},status=status.HTTP_202_ACCEPTED)
                except e:
                    # in case it could not be created
                    return Response({"message":"Accept Invite Unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message":"Accept Invite Unsuccessful: association does not exist"},status.HTTP_404_NOT_FOUND)
            
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found"},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message":"Could not create contact association"}, status=status.HTTP_204_NO_CONTENT)
    
    