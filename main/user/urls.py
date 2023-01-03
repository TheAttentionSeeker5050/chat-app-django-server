from django.urls import include, path

# auth
from rest_framework.authtoken.views import obtain_auth_token
from user.API.views.auth.register import RegisterAPIView
from user.API.views.profile.userProfile import UserProfileDetail
from user.API.views.contacts.findUsers import FindContactsView
from .views import AddMockUsers

urlpatterns = [
    path('login', obtain_auth_token, name='api_token_auth'),
    path("register", RegisterAPIView.as_view(), name="register_user"),
    path("profile", UserProfileDetail.as_view(), name="user_profile"),
    path("contacts/find-users", FindContactsView.as_view(), name="find_users"),
    
    path("add_mock_users", AddMockUsers.as_view(), name="add_mock_users"),
]
