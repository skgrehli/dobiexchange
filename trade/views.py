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
from trade.authentication import AccessKeyAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import api_view
from app.models import Key


class OrderList(APIView):
    # import pdb; pdb.set_trace()
    @api_view(["GET","POST"])
    @login_required
    

    def post(self, request, format=None):
        queryset = Key.objects.all()
        key = self.request.query_params.get('access_key', None)
        if key is not None:
            queryset = queryset.filter(access_key=access_key)
        serializer = queryset    
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 1,
                             'message': "",'data':serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MyOrderList(APIView):
    @api_view()
    @login_required
    def get_queryset(self):
        data = OrderedDict()
        queryset = Key.objects.all()

        
        data['key'] = self.request.query_params.get('access_key',)
        data['order_id']= self.request.query_params.get('order_id')
        data['number']= self.request.query_params.get('number')
        data['numberdeal'] = self.request.query_params.get('numberdeal')
        data['price ']= self.request.query_params.get('price')
        data['created'] = self.request.query_params.get('created')
        data['status ']= self.request.query_params.get('status')
        data['market ']= self.request.query_params.get('market') 
        result = data
        return Response({'status':'1','msg':'success','data':result })

    
    
class RuleList(APIView):
    def get(self, request, format=None):
        queryset = Key.objects.all()
        data['key'] = self.request.query_params.get('access_key',)
        data['price_decimal_limit']= self.request.query_params.get('price_decimal_limit')
        data['number_decimal_limit']= self.request.query_params.get('number_decimal_limit')
        data['min'] = self.request.query_params.get('min')
        data['max ']= self.request.query_params.get('price')
        data['buy_rate'] = self.request.query_params.get('buy_rate')
        data['sell_rate ']= self.request.query_params.get('sell_rate')
        data['market ']= self.request.query_params.get('market')
       
        
        result = data
        return Response({'status':'1','msg':'success','data':result })
    def post(self, request, format=None):
        serializer = RuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,
                             'message': "Added successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class CencelList(APIView):
#     def get(self, request, format=None):
#         cencels = Cencel.objects.all()
#         serializer = CencelSerializer(cencels, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CencelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': True,
#                              'message': "Added successfully"},
#                             status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)