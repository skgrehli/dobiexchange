from django.db import models

# Create your models here.
class User(models.Model):
    
   
    username = models.CharField(max_length=80, blank=True)
    email = models.EmailField(('email address'), blank=True, null=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    password = models.CharField(max_length=80, blank=True)
    is_action = models.BooleanField(default=False)
    is_phone_number_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) 
     
   
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    
    def __str__(self):              # __unicode__ on Python 2
        return self.email if  self.email else str(self.phone_number)


class Key(models.Model):
    
   
    secret_key = models.CharField(max_length=80, blank=True)
   
    keys = models.CharField( max_length=30, blank=True)
   
   
    

    
    def __str__(self):            
        return self.keys      