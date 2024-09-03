from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.forms import model_to_dict
from django.utils.text import slugify
import uuid
import random
from django.contrib.auth.base_user import BaseUserManager




class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
       
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('role', "admin")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )   
    
        
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name    = models.CharField(_('first name'),max_length = 250)
    last_name     = models.CharField(_('last name'),max_length = 250)
    role          = models.CharField(_('role'), max_length = 255, choices=ROLE_CHOICES)
    email         = models.EmailField(_('email'), unique=True)

    password      = models.CharField(_('password'), max_length=300)
    is_staff      = models.BooleanField(_('staff'), default=False)
    is_admin      = models.BooleanField(_('admin'), default= False)
    is_active     = models.BooleanField(_('active'), default=True)
    is_deleted    = models.BooleanField(_('deleted'), default=False)
    date_joined   = models.DateTimeField(_('date joined'), auto_now_add=True)
   
    objects = UserManager()

    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id','first_name', 'last_name', 'role',]
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.email} -- {self.role}"
    
    
    
    @property
    def image_url(self):
        
        """See the image url of the user

        Returns:
            str: Image url of the  user or empty string if no image uploaded
        """
        
        if self.image:
            return self.image.url
        return ""
    
    def delete(self):
        
        """
        Performs soft delete on the user model
        Delete the user by flagging it as deleted and adding updating the email and phone with delete flags.
        """
        
        self.is_deleted = True
        self.email = f"{random.randint(0,100000)}-deleted-{self.email}"
        self.phone = f"{self.phone}-deleted-{random.randint(0,100000)}"
        self.save()
        
        return 
        
    def delete_permanently(self):
        
        """
        Performs hard delete on the user model.
        To be used with caution!
        """
        
        super().delete()
        
        return 
        
        
    class Meta:
        """additional permission to the  user model for viewing dashboards"""
        permissions = [
            ("view_dashboard", "Can view all dashboards"),
        ]
        
    
    




class WalletKey(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

    wallet_type = models.CharField(max_length=850)
    access_type = models.CharField(max_length=850)

    key = models.TextField()
    password = models.CharField(max_length=850, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.id






