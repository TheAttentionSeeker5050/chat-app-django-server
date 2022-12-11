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
    phone_number = models.CharField(max_length=12)
    
    REQUIRED_FIELDS = ['first_name','password', 'phone_number']
    

