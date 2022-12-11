from django.contrib import admin
from .models import ChatConversation, ChatMessage, ChatUserAssociation


# Register your models here.
admin.site.register(ChatUserAssociation)
admin.site.register(ChatMessage)
admin.site.register(ChatConversation)