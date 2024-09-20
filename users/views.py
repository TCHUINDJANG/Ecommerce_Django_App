from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from  .serializer import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

import random
import  re



# Générer la vue de session

def generate_session_token(lenght=10):
    char_list = [chr(i) for i in range(97,123)]
    int_list = [str(i) for i in range(10)]
# creer un token

# Créer un jeton unique
    return ''.join(random.SystemRandom().choice(char_list + int_list) for _ in range(lenght))

@csrf_exempt 
def sign(request):
    if not request.method =='POST':
        return JsonResponse({'error':"vous n'etes pas eligibles a vous connecter"})
    
    username = request.POST['email']
    password = request.POST['password']

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error':"Enter a valid Email"})
    
    if len(password) < 6 :
        return JsonResponse({'error':"Password must be 6 character long"})
    
    userModel = get_user_model()

    try:
        user = userModel.objects.get(email=username)

        if user.check_password(password):
            user_dict = userModel.objects.filter(email=username).values().first()
            user_dict.pop('password')

# Si session_token n'est pas 0, il est déjà en cours d'exécution (l'utilisateur est connecté)
        if user.session_token != '0':
            # Si l'utilisateur n'est pas connecté, nous définissons session_token sur 0
            user.session_token = '0'
# Enregistrer la session
            user.save()
            return JsonResponse({'error':"Previous session exists"})
        # Générer un jeton de session
            token = generate_session_token()
            user.session_token = token
            user.save()
            # Connexion de l'utilisateur
            login(request , user)

            return JsonResponse({'token':token, 'user':user_dict})

        else :
            return JsonResponse({'token':'Invalid password'})


    except userModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})
    


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


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create' : [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer


    def get_permissions(self):
        try:
            # Return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            # If action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


# Create your views here.
