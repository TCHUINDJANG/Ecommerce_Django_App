from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from . import models
from rest_framework.decorators import api_view
from . import models
from rest_framework.views import APIView
from rest_framework import status
from .serialize import CategorieSerializer, ProduitsSerializer, PanierSerializer, ArticleDuPanierSerializer, CommandeSerializer, DetailCommandeSerializer, AvisSerializer, UserSerializer,TransactionSerializer, ExpeditionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
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
    


#http://localhost:8000/products/
    
    def get_all_product(self , request ,*args, **kwargs ):
        queryset = self.get_queryset()
        produitSerializer = ProduitsSerializer(queryset, many=True)
        return Response(produitSerializer.data)
    
#http://localhost:8000/products/1/

    def search_product_by_id(self , request ,*args, **kwargs):
        produit = self.get_object()
        produit_serialiser = ProduitsSerializer(produit)
        return Response(produit_serialiser.data)

    
# http://localhost:8000/products/?price__gt=20
    def search_product_by_price(self , request , price):
        queryset = self.get_queryset().filter(price__gt=price)
        product_serializer = ProduitsSerializer(queryset , many=True)
        return Response(product_serializer.data)
    

    def search_product_by_category(self, request , category):
        queryset = self.get_queryset().filter(category__gt=category)
        product_serializer = ProduitsSerializer(queryset)
        return Response(product_serializer.data)
    

        
    def count_products(self , request,*args, **kwargs ):
        count =  produits.objects.count()
        produit_serializer = ProduitsSerializer(count)
        return Response ({"Le nombre total de produit est": produit_serializer} , status=status.HTTP_200_OK)
    
# Tri par défaut  http://localhost:8000/products/?stock__gt=0
    def get_product_by_stock_superieur_at_zero(self , request,*args, **kwargs ):
        queryset = self.get_queryset().filter(stock__gt=0)
        produit_serializer = ProduitsSerializer(queryset, many=True)
        return Response(produit_serializer.data)
    
# http://localhost:8000/products/?search=chaussures
    
    def get_product_by_nom(self , request,*args, **kwargs):
        search_item = request.query_params.get('search' , None)
        if search_item:
            queryset = self.get_queryset().filter(name__contains=search_item)
        else:
            queryset = self.queryset()
        ProduitsSerializer = ProduitsSerializer(queryset , many=True)
        return Response(ProduitsSerializer.data)    


    

class categoryViewSet(viewsets.ModelViewSet):
    queryset =  Category.objects.all() 
    serializer_class = CategorieSerializer

    def create(self , request , *args , **kwargs):
        category_data = JSONParser().parse(request)
        category_serialize = CategorieSerializer(data = category_data)
        if category_serialize.is_valid():
            category_serialize.save()
            return Response({"message": "Ajout de la categorie avec succès"}, status=status.HTTP_201_CREATED)
        return Response(category_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self , request, *args , **kwargs):
        category_data = JSONParser().parse(request)
        category = self.get_object()
        category_serialize = CategorieSerializer(category , data=category_data)
        if category_serialize.is_valid():
            category_serialize.save()
            return Response({"message": "Mise à jour réussie"}, status=status.HTTP_200_OK)
        return Response(category_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response({"message": "Categorie supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    





    
class commandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    def create(self, request, *args, **kwargs):
        commande_data = JSONParser().parse(request)
        commande_serialize = CommandeSerializer(data =commande_data )
        if commande_serialize.is_valid():
            commande_serialize.save()
            return Response({"message": "commande avec succès"}, status=status.HTTP_201_CREATED)
        return Response(commande_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def update(self , request, *args , **kwargs):
        commande_data = JSONParser().parse(request)
        commande = self.get_object()
        commande_serialize = CategorieSerializer(commande , data=commande_data)
        if commande_serialize.is_valid():
            commande_serialize.save()
            return Response({"message": "Mise à jour réussie"}, status=status.HTTP_200_OK)
        return Response(commande_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, *args, **kwargs):
        commande = self.get_object()
        commande.delete()
        return Response({"message": "Categorie supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    
    

























    

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
