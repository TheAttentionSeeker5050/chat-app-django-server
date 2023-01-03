
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
    """Retrieve and edit user profile data"""
    
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
    
    def put(self, request, format=None):
        """This will edit user data"""
        user = user.get_object(request.user)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            # save new data to user profile and return response
            serializer.save()
            return Response(serializer.data)
        # in case that the serializer fields return an exception
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, format=None):
        # this will delete the account
        user = self.get_object(request.user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)