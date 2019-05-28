
from __future__ import unicode_literals
import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db.models import signals




# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        abstract=True



# mobile = PhoneNumberField(required=True, country='+91')
class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username ')
        # username=self.username
        user = self.model(
            username=username, 
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            username=username, email=email,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        # import pdb; pdb.set_trace()

        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,email=email,
            password=password,
        )
        user.email=email
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin, Timestamp):
    
    username = models.CharField(max_length=80,  unique=True)
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)

    is_action = models.BooleanField(default=False)
    is_username_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) 
     
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

   
    def is_admin(self):
        "Is the user a admin member?"
        return self.is_admin

    
    def is_active(self):
        "Is the user active?"
        return self.is_active

    def __str__(self):              # __unicode__ on Python 2
        return self.email if  self.email else str(self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

 
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff

   
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin

    
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active


    def user_post_save(sender, instance, signal, *args, **kwargs):
        #import pdb; pdb.set_trace()
        if not instance.is_verified:
            # Send verification email
            send_verification_email(instance.pk)
     
        signals.post_save.connect(user_post_save, sender=User)
    #instance.post.save()

