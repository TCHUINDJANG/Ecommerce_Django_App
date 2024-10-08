from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser   # a importer dans mon tuto
from rest_framework import status
# from . import models
from rest_framework.decorators import api_view
from . import models
from rest_framework.views import APIView
from rest_framework import status
from .serialize import CategorieSerializer, ProduitsSerializer, PanierSerializer, ArticleDuPanierSerializer, CommandeSerializer, DetailCommandeSerializer, AvisSerializer, UserSerializer,TransactionSerializer, ExpeditionSerializer
from rest_framework import viewsets
from rest_framework.response import Response   # a importer
from .models import *   # a importer   importer egalement la ligne 10
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class produitViewSet(viewsets.ModelViewSet):
    queryset = produits.objects.all()
    serializer_class = ProduitsSerializer
#http://localhost:8000/products/
    def create(self, request, *args, **kwargs):
        produit_data = JSONParser().parse(request)
        produit_serializer = ProduitsSerializer(data=produit_data)
        if produit_serializer.is_valid():
            produit_serializer.save()
            return Response({"message": "Ajout du produit avec succès"}, status=status.HTTP_201_CREATED)
        return Response(produit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        produit_data = JSONParser().parse(request)
        produit = self.get_object()
        produit_serializer = ProduitsSerializer(produit, data=produit_data)
        if produit_serializer.is_valid():
            produit_serializer.save()
            return Response({"message": "Mise à jour réussie bravo"}, status=status.HTTP_200_OK)
        return Response(produit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        produit = self.get_object()
        produit.delete()
        return Response({"message": "Produit supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    



    

    

























    

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_data = JSONParser().parse(request)
        user_serialize = UserSerializer(data=user_data)
        if user_serialize.isvalid():
            user_serialize.save()
            return Response({"message": "commande avec succès"}, status=status.HTTP_201_CREATED)
        return Response(user_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

class panierViewSet(viewsets.ModelViewSet):
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer

    def create(self , request ,*args, **kwargs ):
        panier_data = JSONParser().parse(request)
        panier_serialize = PanierSerializer(data=panier_data)
        if panier_serialize.is_valid():
            panier_serialize.save()
            return Response({"message": "article ajoute dans le panier avec succès"}, status=status.HTTP_201_CREATED)
        return Response(panier_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

    



        
    



 

       

 

    
    
 

# Create your views here.
