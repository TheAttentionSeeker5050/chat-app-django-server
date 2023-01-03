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
    

class UserContacts(models.Model):
    """
    This model associates users as contacts, should contain:
    user1, user2 (they both conform into a composite key)
    date request was accepted
    request_accepted (boolean)
    """
    user1 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+")
    user2 = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE, default=False, related_name="+")
    contacts_since = models.DateField()
    request_accepted = models.BooleanField(blank=False)
