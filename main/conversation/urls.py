from django.urls import include, path
"""
These urls will consist of the following:
create new conversation, if not blacklisted
drop conversation
change conversation params
create message within conversation
get all messages in conversation
edit message in conversation
drop message in conversation
"""
from conversation.API.conversationsView.privateConversationViews import PrivateConversationView
urlpatterns = [
    path("private", PrivateConversationView.as_view(), name="private_conversation"),
]