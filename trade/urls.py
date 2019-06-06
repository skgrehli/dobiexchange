#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.conf.urls import url

# Rest Framework imports.

from trade.views import *


app_name = 'trade'

urlpatterns = [
    
  	
    url(r'^order/$', OrderList.as_view(), name='order'),
    url(r'^myorder/?<market>/<commonparameters>/<page>/<sortType>/<orderIds>/<starttime>/<endtime>$', MyOrderList.as_view(), name='myorder'),
    url(r'^rules/?<market>$', RuleList.as_view(), name='rules'),
    # url(r'^cencel/$', CencelList.as_view(), name='cencel'),

]