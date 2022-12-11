from user.models import AppUser
from rest_framework import serializers

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, max_length=60)
    email = serializers.EmailField(allow_null=False)
    first_name = serializers.CharField(max_length=50, allow_null=True, required=False)
    last_name = serializers.CharField(max_length=50, allow_null=True, required=False)
    phone_number = serializers.CharField(max_length=12, allow_null=True, required=False)
    password = serializers.CharField(max_length=120, allow_null=False)
    # password_confirmation = serializers.CharField(max_length=120, allow_null=False)
    
    class Meta:
        extra_kwargs = {
            "password": {"write_only":True},
            "password_confirmation": {"write_only":True},
        }
        
    def validate_password(self, value):
        """Make sure that the password is valid"""
        data = self.get_initial()
        # print(data)
        password = data.get("password")
        password_confirmation = value
        # print("password:", password, "\npassword confirmation:", password_confirmation)
        
        if password != password_confirmation:
            # return False
            raise ValueError("Passwords must match")
        return value
    
        
    def create(self, validated_data):
        user = AppUser.objects.create(
            **validated_data
            )
        user.set_password(validated_data["password"])
        user.save()
        return user
        # return AppUser.objects.create(
        #     **validated_data
        #     )