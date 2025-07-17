from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework import status

# Create your views here.

class UserView(APIView):
    def post(self,request):
        new_user=User(username=request.data['username'],is_superuser=request.data['is_superuser'])
        new_user.set_password(request.data['password'])

        new_user.save()

        return Response('New user created')
    
class UserLoginView(APIView):
    def post(self,request):

        user_data=CustomToken_Serializer(data=request.data)

        if user_data.is_valid():
            return Response(user_data.validated_data)
        else:
            return Response(user_data.errors ,status=404)

        '''  this code use to validate the user data without jwt token ,with jwt token use serializers & above code format

        user_verification=authenticate(username=request.data['username'],password=request.data['password'])

        if user_verification==None:
            return Response('Username or password is not valid')
        
        else:
            return Response('Valid user') '''