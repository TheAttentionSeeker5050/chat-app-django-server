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
    
    conversation_id = models.ForeignKey(ChatConversation, on_delete=models.CASCADE)
    MESSAGE_TYPE_CHOICES = [
        ("TEXT", "Text"),
        ("IMG", "Image"),
        ("VIDEO", "Video"),
        ("AUDIO", "Audio"),
        ("DOCUMENT", "Document"),
    ]
    
    message_type = models.CharField(
        max_length=60, choices=MESSAGE_TYPE_CHOICES)
    message_text = models.TextField()
    message_media_address = models.TextField(max_length=500)
    creation_date = models.DateField()
    edition_date = models.DateField()
    
    
class ChatUserAssociation(models.Model):
    """
    This contains each user associated with conversation
    """
    
    conversation_id = models.ForeignKey(ChatConversation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)