from django.db import models

# Create your models here.
class ChatConversation():
    """
    This model should contain:
    conversation Id, 
    conversation name, 
    type attribute direct_message (True or False)
    """
    
    
class ChatMessage():
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