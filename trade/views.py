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

from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import generics
#from keys.utils import generate_jwt_token,verify_token,generate_jwt_token_only
# from app.utils import generate_jwt_token
# local imports
from django.contrib.auth.decorators import login_required
from trade.serializers import *

from trade.models import Order


class OrderList(APIView):
    def get(self, request, format=None):
        # import pdb;pdb.set_trace()
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({'status':'1','msg':'success','data': serializer.data})
        # return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# 
class MyOrderList(APIView):
    
    def get(self, request, format=None):
        myorders = MyOrder.objects.all()
        serializer = MyOrderSerializer(myorders, many=True)
        # return Response(serializer.data)
        return Response({'status':'1','msg':'success','data': serializer.data})

    # @login_required
    def post(self, request, format=None):
        serializer = MyOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RuleList(APIView):
    def get(self, request, format=None):
        rules = Rule.objects.all()
        serializer = RuleSerializer(rules, many=True)
        return Response({'status':'1','msg':'success','data': serializer.data})

    def post(self, request, format=None):
        serializer = RuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CencelList(APIView):
    def get(self, request, format=None):
        cencels = Cencel.objects.all()
        serializer = CencelSerializer(cencels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CencelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)