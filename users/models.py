from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
import jwt
from django.conf import settings
from django.utils import timezone
import secrets
import string
from datetime import timedelta


# Create your models here.


class CustomUser(AbstractUser):

    name = models.CharField(max_length=50, default='Anonymous' , blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    session_token = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='account/profile', blank=True)
    address = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # ceci sera utilisé pour connecter les utilisateurs au lieu du nom d'utilisateur
    REQUIRED_FIELDS = []   # ceci est destiné à l'administrateur lors de la création du superutilisateur




class FailedEmailTasks(models.Model):
    task_id = models.CharField(max_length=255)
    exc = models.TextField()
    args = models.JSONField()
    kwargs = models.JSONField()
    einfo = models.TextField()



def get_confirmation_token(self):
    return self.generate_password_reset_account_validation_token()


def generate_password_reset_account_validation_token(self):
        values = string.ascii_letters + string.digits
        token = "".join(secrets.choice(values) for _ in range(250))
        dt = timezone.now() + timedelta(seconds=settings.CONFIRMATION_LINK_TIMEOUT)
        encode_token = jwt.encode(
            {"token": token, "exp": int(dt.strftime("%s")), "id": self.id},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return encode_token