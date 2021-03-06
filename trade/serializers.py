#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python imports.
import logging
import datetime
import calendar

# Django imports.
from django.db import transaction 

# Rest Framework imports.
from rest_framework import serializers
from trade.models import *
# Third Party Library imports

# local imports.





class OrderSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    type = serializers.CharField(max_length=50)
    market = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=4, decimal_places=4)

    number = serializers.IntegerField()
    class Meta:
        
        fields = ('id', 'type','price','market' ,'number')


# class MyOrderSerializer(serializers.ModelSerializer):

#     class Meta:
#         fields = ('flag','order_id','number','numberdeal','numberover','price','created','status','market',)


# class RuleSerializer(serializers.ModelSerializer):

#     class Meta:
       
#         fields = ('market','price_decimal_limit','number_decimal_limit','min','max','buy_rate','sell_rate')

# class CencelSerializer(serializers.ModelSerializer):

#     class Meta:
       
#         fields = ('market','order_id')