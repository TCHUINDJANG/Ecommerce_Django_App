from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class Customer(BaseUserManager):
    def create_user(self , email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set') 
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
