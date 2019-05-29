from django.contrib import admin
from trade.models import Order , Rule, MyOrder
# Register your models here.

admin.site.register(Order)
admin.site.register(MyOrder)
admin.site.register(Rule)