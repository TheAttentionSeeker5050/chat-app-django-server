# import serializer
from user.API.serializers.blacklist import BlacklistSerializer
from rest_framework.views import APIView

# import models
from user.models import AppUser, ContactsBlacklist

# http imports
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# authentications
from rest_framework.authentication import TokenAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated

class BlacklistAPIView(APIView):
    """
    This api view will add and remove blacklist entries, this to avoid unwanted users being dm'ed, it will not prevent group conversations from 
    being sent to user where user where an unwanted contact is present
    """
    
    authentication_classes = [TokenAuthentication,]
    
    def post(self, request, contact_username, format=None):
        # first we make sure the blacklist entry doesn't already exist
        try:
            # get app user entries to associate to the user, user 1 is the authenticated user with api key
            user1 = AppUser.objects.get(username=request.user) 
            user2 = AppUser.objects.get(username=contact_username) # user 2 is from the url param contact_username
            
            # now that we have both users we test if there is a previous entry
            test_case_previous_entry_1 = ContactsBlacklist.objects.filter(user1=user1, user2=user2).count()
            test_case_previous_entry_2 = ContactsBlacklist.objects.filter(user1=user2, user2=user1).count()
            
            if (test_case_previous_entry_1==0 and test_case_previous_entry_2==0):
                # now that we made sure that there are not previous queries we add the blacklisted elements
                try:
                    query = ContactsBlacklist.objects.create(user1=user1, user2=user2)
                    query.save()
                    return Response({"message":"Request successfull: User was blacklisted"}, status=status.HTTP_201_CREATED)
                except e:
                    # in case request returned an exception
                    return Response({"message":"Request unsuccessfull: "+e}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":"Request unsuccessful: association already exist"}, status.HTTP_405_METHOD_NOT_ALLOWED)

        except AppUser.DoesNotExist:
            return Response({"message":"Users not found"},status=status.HTTP_404_NOT_FOUND)
        return Response(data={"message":"Could not create blacklist association"}, status=status.HTTP_400_BAD_REQUEST)
    
  
    def delete(self, request, contact_username, format=None):
        # when we want to de-blacklist a contact, meaning we want to remove the blacklist entry from the contact
        try:
            # get app user entries to associate to the user, user 1 is the authenticated user with api key
            user1 = AppUser.objects.get(username=request.user) 
            user2 = AppUser.objects.get(username=contact_username) # user 2 is from the url param contact_username
            
            # now that we have both users we test if there is a previous entry
            test_case_previous_entry_1 = ContactsBlacklist.objects.filter(user1=user1, user2=user2).count()
            test_case_previous_entry_2 = ContactsBlacklist.objects.filter(user1=user2, user2=user1).count()
            
            if (test_case_previous_entry_1==0 and test_case_previous_entry_2==0):
                # in this case the entry does not exist, meaning that we cannot delete the user association
                return Response({"message":"Request unsuccessful: association doesn't exist"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                # in this case the user association could be created
                
                # delete user association only user that made the blacklist request can de-blacklist
                instance = ContactsBlacklist.objects.get(user1=user1, user2=user2)
                instance.delete()
                return Response({"message":"Request successful: Element could be deleted"}, status=status.HTTP_200_OK)
        
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found"},status=status.HTTP_404_NOT_FOUND)
        return Response(data={"message":"Could not create blacklist association"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, contact_username, format=None):
        # we get the blacklisted entry for permissions purposes, this will be read by middleware
        try:
            
            user1 = AppUser.objects.get(username=request.user) 
            user2 = AppUser.objects.get(username=contact_username) # user 2 is from the url param contact_username
        
            test_case_previous_entry_1 = ContactsBlacklist.objects.filter(user1=user1, user2=user2).count()
            test_case_previous_entry_2 = ContactsBlacklist.objects.filter(user1=user2, user2=user1).count()
            
            if (test_case_previous_entry_1>=1):
                return Response(data={"message": "Contact was blacklisted by user", "is_blacklisted": True, "is_blacklisted_by_user": True, "returned_exception":False})
            elif (test_case_previous_entry_2>=1):
                return Response(data={"message": "Contact blacklisted you", "is_blacklisted":True, "is_blacklisted_by_user": False, "returned_exception":False})
            else:
                return Response(data={"message": "Contact is not blacklisted", "is_blacklisted":False, "is_blacklisted_by_user": False, "returned_exception":False})
            
            
            return Response(data={"message":"Request returned exception", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
        
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found" , "returned_exception":True},status=status.HTTP_404_NOT_FOUND)
        return Response(data={"message":"Request returned exception", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)