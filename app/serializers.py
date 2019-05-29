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
from app.models import *
# Third Party Library imports

# local imports.




class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
       return super(UserCreateSerializer, self).validate(data, *args, **kwargs)


    def create(self, validated_data):
        
        usrename = validated_data.get('usrename')
        first_name = validated_data.get('first_name')
        name = validated_data.get('name')
    
        email = validated_data.get('email')
        is_action = False
        is_email_verified = False
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user

    class Meta:
        model = User
        fields = ('id','email', 'password', 'username', 'first_name','name')


class KeySerializer(serializers.ModelSerializer):

    class Meta:
        model = Key
        fields = ('id', 'access_key','secret_key','exchange_name' )
