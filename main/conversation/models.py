from django.db import models
from user.models import AppUser


# Create your models here.
class ChatConversation(models.Model):
    """
    This model should contain:
    conversation Id, 
    conversation name, 
    type attribute direct_message (True or False)
    """
    
    conversation_name = models.CharField(max_length=120, null=True, blank=True)
    creation_date = models.DateField()
    
class PrivateConversation(models.Model):
    """This model creates a private conversation between only 2 USERS ONLY"""
    user_1_id = models.ForeignKey(AppUser,related_name="user_1", on_delete=models.CASCADE)
    user_2_id = models.ForeignKey(AppUser, related_name="user_2", on_delete=models.CASCADE)
    creation_date = models.DateField()
    
    
    
class ChatMessage(models.Model):
    """
    This model should contain:
    Conversation id foreign key
    user foreign key
    message content
    message type (for now it is text, but it may later be multimedia objects)
    message date
    message edition date
    message_edited (True)
    """
    user_id = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False)
    group_conversation_id = models.ForeignKey(ChatConversation, default=None, on_delete=models.CASCADE)
    MESSAGE_TYPE_CHOICES = [
        ("TEXT", "Text"),
        ("IMG", "Image"),
        ("VIDEO", "Video"),
        ("AUDIO", "Audio"),
        ("DOCUMENT", "Document"),
    ]
    
    message_type = models.CharField(
        max_length=60, choices=MESSAGE_TYPE_CHOICES, default="TEXT")
    message_text = models.TextField()
    message_media_address = models.TextField(max_length=500)
    creation_date = models.DateField()
    edition_date = models.DateField()
    private_conversation_id = models.ForeignKey(PrivateConversation, default=None, on_delete=models.CASCADE)
    
    
class ChatUserAssociation(models.Model):
    """
    This contains each user associated with conversation group between any number of users
    """
    
    conversation_id = models.ForeignKey(ChatConversation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)