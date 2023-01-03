
# import serializer
from user.API.serializers.userProfile import UserProfileSerializer
from rest_framework.views import APIView

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

# class FindUsersView(APIView):
#     """Retrieve and edit user profile data"""
    
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [IsAuthenticated,]
    
                
#     def get(self, request, format=None):
#         queryset = AppUser.objects.all()
        
#         return Response(serializer.data)

from rest_framework import generics

class FindContactsView(generics.ListAPIView):
    """Get a list of the main users matching the search criteria"""
    
    queryset = AppUser.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', "first_name", "last_name"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    
class ContactDetailView(APIView):
    """
    Get the detail view of a contact the user clicked or tapped on
    """