# import serializer
from user.API.serializers.contact import ContactBookSerializer
from rest_framework.views import APIView
from rest_framework import generics

# import models
from user.models import AppUser
from user.models import ContactBook

# http imports
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# authentications
from rest_framework.authentication import TokenAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated


# django filters
from rest_framework import filters

class ContactBookView(APIView):
    """
    Create, get or delete contact book associations for users
    """
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, contact_username, format=None):
        """
        get the contact book data from user and url param
        """
        
        try:
            # get app user entries to associate to the user, user 1 is the authenticated user with api key
            user1 = AppUser.objects.get(username=request.user) 
            user2 = AppUser.objects.get(username=contact_username) # user 2 is from the url param contact_username
            
            test_case_previous_entry = ContactBook.objects.filter(user1=user1, user2=user2).count()
            
            if (test_case_previous_entry==0):
                
                # if contact association does not exist yet, save contact
                try:
                    query = ContactBook.objects.create(user1=user1, user2=user2)
                    query.save()
                    return Response({"message":"The user was added to your contacts", "returned_exception":False}, status=status.HTTP_201_CREATED)
                
                except e:
                    # in case request returned an exception
                    return Response({"message":"Request unsuccessfull: "+e, "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # if contact was already saved, return error
                return Response({"message":"Request unsuccessfull: Contact association already exist", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
                
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found", "returned_exception":True},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"Could not save to contacts", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, contact_username, format=None):
        """
        Delete contact from the database
        """
        
        try:
            # get app user entries to associate to the user, user 1 is the authenticated user with api key
            user1 = AppUser.objects.get(username=request.user) 
            user2 = AppUser.objects.get(username=contact_username) # user 2 is from the url param contact_username
            
            try:
                    instance = ContactBook.objects.get(user1=user1, user2=user2)
                    instance.delete()
                    return Response({"message":"The user was deleted from your contacts", "returned_exception":False}, status=status.HTTP_200_OK)
            except:
                # in case request returned an exception
                return Response({"message":"Could not delete contact", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
            
        except AppUser.DoesNotExist:
            return Response({"message":"Users not found", "returned_exception":True},status=status.HTTP_404_NOT_FOUND)
        return Response(data={"message":"Could not make changes", "returned_exception":True}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        """Get all the users contacts"""
        user1 = AppUser.objects.get(username=request.user) 
        
        contacts = ContactBook.objects.all(user1=user1)
        serializer = ContactBookSerializer(contacts, many=True)
        return Response(serializer.data)
    

    
# class ContactBookListView(APIView):
#     """
#     Create, get or delete contact book associations for users
#     """
#     def get(self, request, format=None):
#         queryset = ContactBook.objects.filter(user1__username=request.user)
#         return Response(data={"data":queryset})
    
    # def get(self, request, format=None):
    #     """Get all the users contacts"""
    #     user1 = AppUser.objects.get(username=request.user)
        
    #     contacts = ContactBook.objects.filter(user1__username=user1.username)
    #     print(contacts[:])
    #     # serializer = ContactBookSerializer(contacts[:], many=True)
    #     return Response(data={"response":"contacts"})
    
    # class ContactBookListView(generics.ListAPIView):
    # """
    # Create, get or delete contact book associations for users
    # """
    # model = ContactBook
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # serializer_class = ContactBookSerializer
    
    # def get_queryset(self):
    #     user = self.request.user
        
    #     return ContactBook.objects.filter(user1__username=user)