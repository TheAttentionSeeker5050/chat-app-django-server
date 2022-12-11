
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

class UserProfileDetail(APIView):
    """Retrieve user profile data"""
    
    authentication_classes = [TokenAuthentication,]
    
    def get_object(self, user):
        try:
            return AppUser.objects.get(username=user)
        except AppUser.DoesNotExist: 
            raise Http404
                
    def get(self, request, format=None):
        user = self.get_object(request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)