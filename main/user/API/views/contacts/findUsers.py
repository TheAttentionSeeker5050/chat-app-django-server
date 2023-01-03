
# import serializer
from user.API.serializers.contact import ContactSerializer
from rest_framework.views import APIView
from rest_framework import generics

# import models
from user.models import AppUser

# http imports
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# authentications
from rest_framework.authentication import TokenAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated

# django filters
from rest_framework import filters




class FindContactsView(generics.ListAPIView):
    """Get a list of the main users matching the search criteria"""
    
    queryset = AppUser.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', "first_name", "last_name"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    
class ContactDetailView(APIView):
    """
    Get the detail view of a contact the user clicked or tapped on
    we should also see if the user is already our contact
    """
    
    def get_object(self, contact_username):
        """Get an user object by it's email, which is unique"""
        try:
            return AppUser.objects.get(username=contact_username)
        except AppUser.DoesNotExist:
            raise Http404
    
    def get(self, request, contact_username, format=None):
        """Get detailed user profile"""
        user = self.get_object(contact_username) # get user by email in request body
        # serializer = UserProfileSerializer(user, data=request.data)
        serializer = ContactSerializer(user)
        return Response(serializer.data)
    
    