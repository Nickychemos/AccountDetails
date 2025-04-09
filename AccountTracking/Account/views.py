from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Account
from .serializer import AccountSerializer

# Create your views here. (APIViews)

class AccountAPIView(viewsets.ModelViewSet):
    #A get function to obtain data
    def list(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many = True)
        return Response(serializer.data)
    
    #A post function to register new users
    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status =status.HTTP_400_BAD_REQUEST)
    
    #View to get specific items
    def retrieve(self, request, id):
        try:
            Account = Account.objects.get(id = id)
        except Account.DoesNotExist:
            return Response({"error": "Item Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(Account, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    #Patching an account (Updating)
    def update(self, request, id):
        try:
            Account = Account.objects.get(id = id)
        except Account.DoesNotExist:
            return Response({"Error": "Account Not Found"}, status=status.HTTP_404_NOT_FOUND)
        #partially updating
        serializer = AccountSerializer(Account, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #deleting an account
    def destroy(self, request, id):
        try:
            Account = Account.objects.get(id=id)
        except Account.DoesNotExist:
            return Response({"Error":"Account Does not Exist"}, status=status.HTTP_404_NOT_FOUND)
        
        Account.delete()
        return Response({"detail": "Account has been deleted successfully"}, status= status.HTTP_204_NO_CONTENT)
            