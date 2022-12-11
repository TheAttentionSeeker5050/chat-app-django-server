from user.models import AppUser
from rest_framework import serializers

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=60)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_lenght=12)
    password = serializers.CharField(max_lenght=120, blank=False)
    password_confirmation = serializers.CharField(max_lenght=120, blank=False)
    
    class Meta:
        extra_kwargs = {
            "password": {"write_only":True},
            "password_confirmation": {"write_only":True},
        }
        
    def validate_password(self, value):
        """Make sure that the password is valid"""
        data = self.get_initial()
        password = data.get("password_confirmation")
        password_confirmation = value
        
        if password != password_confirmation:
            raise ValueError("Passwords must match")
        return value
    
    
    def validate_password2(self, value):
        """Make sure that the password confirmation is valid"""
        data = self.get_initial()
        password = data.get("password")
        password_confirmation = value
        
        if password != password_confirmation:
            raise ValueError("Passwords must match")
        return value