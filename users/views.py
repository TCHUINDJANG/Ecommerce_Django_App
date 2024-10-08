from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from  produit.serialize import UserSerializer
from users.serialize import UserSerializers
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import random
import  re
from rest_framework.response import Response
from django.conf import settings
from rest_framework import serializers



# Générer la vue de session

def generate_session_token(lenght=10):
    char_list = [chr(i) for i in range(97,123)]
    int_list = [str(i) for i in range(10)]
# creer un token

# Créer un jeton unique
    return ''.join(random.SystemRandom().choice(char_list + int_list) for _ in range(lenght))

api_view(["POST"])
@permission_classes([AllowAny])           #  http://127.0.0.1:8000/api//api/users/
def RegistrationView(request)  -> Response:
     with transaction.atomic():
        try:
             
    #     subject = "Ecoms Welcome Mail"
    #     message = ""  # this is needed to be empty although html message is to be sent
    #     from_email = "noreply@example.com"
    #     recipient_list = [instance.email]
    #     generated_token = instance.get_confirmation_token
    #     # Render the HTML template
    #     html_message = render_to_string(
    #          "welcome_mail.html",
    #          {"request": request, "username": instance.username, "confirm_token": generated_token},
    #      )
    #    send_email_task.delay(subject, message, from_email, recipient_list, html_message=html_message)
            serializer = UserSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.set_rollback(True)
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST,
            )
    
   
@api_view(["GET"])
@permission_classes([AllowAny])
def ConfirmRegistration(request):
    token = request.GET.get("token")
    # redirect user to page to tell them to request for new validation email
    if not token:
        return redirect(settings.CONFIRMATION_MAIL_REQUEST_PAGE)
    # get user id
    user_id, error = decode_jwt(token)
    if user_id and error is None:
        user = CustomUser.objects.filter(id=user_id)
        if user.exists():
            user.update(verified=True)
            return redirect(settings.FRONTEND_HOMEPAGE)
    return redirect(settings.CONFIRMATION_MAIL_REQUEST_PAGE)
    

   #  http://127.0.0.1:8000/api/api/logout/
def signout(request , id):

    UserModel = get_user_model()

    try:

        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
        logout(request)
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid User ID'})
    
    return JsonResponse({'success': 'Logout successful'})



# http://127.0.0.1:8000/api//api/forgot-password/


def forgot_password_view(self, request):
        email = request.data.get('email')
        user = user.objects.filter(email=email).first()
        if user:
            # Logique pour envoyer un e-mail de réinitialisation de mot de passe
            return JsonResponse({'message': _('Password reset email sent!')}, status=status.HTTP_200_OK)
        return JsonResponse({'error': _('User not found')}, status=status.HTTP_404_NOT_FOUND)


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes_by_action = {'create' : [AllowAny]}
#     queryset = CustomUser.objects.all().order_by('id')
#     serializer_class = UserSerializer


def get_permissions(self):
        try:
            # Return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            # If action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


# Create your views here.
