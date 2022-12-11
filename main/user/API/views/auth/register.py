"""
This api view(s) are related to user registration
"""

from user.models import AppUser
from user.serializers.register import UserRegisterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(APIView):
    """
    Create a new user, delete or update it
    """
    
    def post(self, request, format=None):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            AppUser(serializer.save)
            return Response({
                "status": "success",
                "code":status.HTTP_201_CREATED, 
                "details": serializer.data
            })
        return Response({
            "status":"unsuccessful", 
            "code":status.HTTP_400_BAD_REQUEST, 
            "details":serializer.errors
        })