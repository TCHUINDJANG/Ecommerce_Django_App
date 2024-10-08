from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .utils import validate_passwords


from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email","username","password","confirm_password",
            "address"]
        


def validate(self  , data):
    password= data.get("password")
    confirm_password = data.get("confirm_password")
    validate_passwords(password, confirm_password)
    del data["confirm_password"]
    return data
         
