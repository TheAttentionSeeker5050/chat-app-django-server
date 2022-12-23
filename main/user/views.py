from django.shortcuts import render
from .models import AppUser
# Create your views here.
"""
Views will be:
user login and register
view user profile
view other's profile
search other users
add or delete other users
upodate profile or delete it.

These should have:
authentications and permissions set
API endpoints
serializers
"""

from django.http import HttpResponse
from django.views import View

# import the mock json data
from .mock_data import mock_json_data




class AddMockUsers(View):
    def get(self, request, *args, **kwargs):
        
        for row in mock_json_data:
            object_instance = AppUser(
                username=row["username"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                password=row["password"],
                phone_number=row["phone_number"],
                bio=row["bio"]
            )
            
            object_instance.save()
        
        # print(mock_json_data[0])
        return HttpResponse("Your elements have been added")