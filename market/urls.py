#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.conf.urls import url

# Rest Framework imports.

from trade.views import *


app_name = 'market'

urlpatterns = [
    
  	
    # url(r'^order/$', OrderList.as_view(), name='order'),
    # url(r'^myorder$', MyOrderList.as_view(), name='myorder'),
    # url(r'^rules/$', RuleList.as_view(), name='rules'),
    # url(r'^cencel/$', CencelList.as_view(), name='cencel'),

]