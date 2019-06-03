#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.conf.urls import url

# Rest Framework imports.

from app.views import *


app_name = 'app'

urlpatterns = [
    url(r'^register/$', RegistrationAPIView.as_view(), name='register-api'),
    url(r'^login/$', LoginView.as_view(), name='login-api'),
    url(r'^logout/$', LogoutView.as_view(), name='logout-api'),
  	
    url(r'^keys/$', KeyList.as_view(), name='keys'),
    url(r'^keys/(?P<pk>[0-9]+)/$', KeyDetail.as_view()),

]