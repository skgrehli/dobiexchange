# Python Imports
import re
import os
import sys
import time
import base64
import copy
import json
import datetime
import requests
import random


# Django imports
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, ValidationError  
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# Rest Framework imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from app.serializers_jwt import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import generics
#from keys.utils import generate_jwt_token,verify_token,generate_jwt_token_only
# from app.utils import generate_jwt_token
# local imports

from .tokens import account_activation_token
from app.models import *
from app.serializers import *
from app.utils import generate_jwt_token
from app.models import User





class RegistrationAPIView(GenericAPIView):
   
    
    serializer_class = UserCreateSerializer

    __doc__ = "Registration API for user"

    def post(self, request, *args, **kwargs):
        
        try:
            user_serializer = UserCreateSerializer(data=request.data)
            
            if user_serializer.is_valid():
                user_serializer.is_active = False
                user = user_serializer.save()
                data = generate_jwt_token(user, user_serializer.data)
                #send_verification_email.delay(user.pk)
                current_site = get_current_site(request)
                
             
                return Response(data, status=status.HTTP_200_OK)

            else:
                message = ''
                for error in user_serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)



class LoginView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer
    
    __doc__ = "Log In API for user which returns token"

    @staticmethod
    def post(request):
        # import pdb;pdb.set_tarce() 
        try:
            serializer = JSONWebTokenSerializer(data=request.data)
            if serializer.is_valid():
               
                serialized_data = serializer.validate(request.data)
                user = User.objects.get(email=request.data.get('email'))
                return Response({
                    'status': True,
                    'token': serialized_data['token'],
                }, status=status.HTTP_200_OK)
                
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)


        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False,
                             'message': "User doesnot exists"},
                            status=status.HTTP_400_BAD_REQUEST)



class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    @staticmethod
    def post(request):
        """
        Logout API for user
        """
        try:
            user = request.data.get('user', None)
            logout(request)
            return Response({'status': True,
                             'message': "logout successfully"},
                            status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False},
                            status=status.HTTP_400_BAD_REQUEST)




class KeyList(APIView):
    def get(self, request, format=None):
        keys = Key.objects.all()
        serializer = KeySerializer(keys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyDetail(APIView):
    
    
    def get_object(self, pk):
        try:
            return Key.objects.get(pk=pk)
        except Key.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        keys = self.get_object(pk)
        keys = KeySerializer(keys)
        return Response(keys.data)

    def put(self, request, pk, format=None):
        keys = self.get_object(pk)
        serializer = KeySerializer(keys, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        keys = self.get_object(pk)
        keys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
