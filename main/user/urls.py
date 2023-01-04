from django.urls import include, path

# auth
from rest_framework.authtoken.views import obtain_auth_token
from user.API.views.auth.register import RegisterAPIView
from user.API.views.profile.userProfile import UserProfileDetail
from user.API.views.contacts.findUsers import FindContactsView, ContactDetailView
from user.API.views.blacklist.blacklistView import BlacklistAPIView
from .views import AddMockUsers

urlpatterns = [
    path('login', obtain_auth_token, name='api_token_auth'),
    path("register", RegisterAPIView.as_view(), name="register_user"),
    # user profile, alter,  delete or view user profile
    path("profile", UserProfileDetail.as_view(), name="user_profile"),
    # other users
    path("contacts/find-users", FindContactsView.as_view(), name="find_other_users"),
    path("contacts/view-user/<str:contact_username>/", ContactDetailView.as_view(), name="contact_detail_view"),
    path("add_mock_users", AddMockUsers.as_view(), name="add_mock_users"),
    # # contact invitations and edits
    path("contacts/blacklist-user/<str:contact_username>/", BlacklistAPIView.as_view(), name="send_user_invite"),
    
    
]
