from django.urls import include, path

# auth
from rest_framework.authtoken.views import obtain_auth_token  


urlpatterns = [
    path('login', obtain_auth_token, name='api_token_auth'),
]
