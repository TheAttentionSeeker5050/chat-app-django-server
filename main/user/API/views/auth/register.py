"""
This api view(s) are related to user registration
"""

from user.models import AppUser
from user.API.serializers.register import UserRegisterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class RegisterAPIView(APIView):
    """
    Create a new user, delete or update it
    """
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        print(request.data, type(request.data))
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validate_password(request.data["password"]):
                
                serializer.save()
                
                return Response({
                    "status": "success",
                    "code":status.HTTP_201_CREATED, 
                    "details": "User created successfully"
                })
            else:
                return Response({
                    "status": "unsuccessful", 
                    "code":status.HTTP_400_BAD_REQUEST, 
                    "details":"Passwords Must Match"
                })
        return Response({
            "status":"unsuccessful", 
            "code":status.HTTP_400_BAD_REQUEST, 
            "details":serializer.errors
        })