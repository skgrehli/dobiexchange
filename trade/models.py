from django.db import models
from decimal import *

# Create your models here.
Type_choice=(
    ('BUY','Buy'),
    ('SELL','Sell'),
    
 )

Status_choice=(
    (0,'uncompleted transactions'),
    (1,'Partial transaction'),
    (2,'Completed Transactions'),
    (3,'Revoked'),
    
 )



class Order(models.Model):
    type = models.CharField(max_length=5,  choices=Type_choice,default='Buy', )     
    
    price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000')) 
    number= models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000')) 
    market = models.CharField(max_length=5, )    

    def __str__(self):       
        return self.type

class MyOrder(models.Model):
    flag  = models.CharField(max_length=5,  choices=Type_choice, ) 
    order_id  = models.ForeignKey(Order, on_delete=models.CASCADE)
    number  = models.IntegerField()
    numberdeal = models.IntegerField()
    numberover = models.IntegerField()
    price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000')) 
    created = models.DateTimeField(auto_now_add=True)
    status =models.IntegerField( choices=Status_choice,default='Buy',) 
    def __str__(self):       
        return self.order_id


class Rule(models.Model):

    market  =models.CharField(max_length=5,)
    price_decimal_limit = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    number_decimal_limit   = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    min  = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    max = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    buy_rate = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    sell_rate  =models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))  
    
    def __str__(self):       
        return self.market