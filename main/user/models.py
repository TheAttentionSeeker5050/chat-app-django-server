from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    """
    The app user model should contain:
    personal information (name, nickname, email and phone number)
    password and recovery data
    bio and profile picture address
    account opening date
    """
    
    # these are the only modified fields so i just add these
    
    bio = models.TextField()
    email = models.EmailField(max_length=35, blank=False, unique=True)
    phone_number = models.CharField(max_length=12, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.username

    
class ContactsBlacklist(models.Model):
    """
    This model allows you to blacklist contacts
    """
    user1 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+")
    user2 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+")
    
class ContactBook(models.Model):
    """
    This model is for adding a contact book
    """
    
    user1 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+", related_query_name="user1")
    user2 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+", related_query_name="user2")