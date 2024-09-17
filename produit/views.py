from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from . import models
from rest_framework.decorators import api_view
from . import models
from rest_framework.views import APIView
from rest_framework import status
from .serialize import CategorieSerializer, ProduitsSerializer, PanierSerializer, ArticleDuPanierSerializer, CommandeSerializer, DetailCommandeSerializer, AvisSerializer, TransactionSerializer, ExpeditionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *

class produitViewSet(viewsets.ModelViewSet):
    queryset = produits.objects.all()
    serializer_class = ProduitsSerializer

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
            return Response({"message": "Mise à jour réussie"}, status=status.HTTP_200_OK)
        return Response(produit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        produit = self.get_object()
        produit.delete()
        return Response({"message": "Produit supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try: 
        produict = produict.objects.get(pk=pk) 
    except produict.DoesNotExist: 
        return JsonResponse({'message': 'The produict does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
       produit_serialize = ProduitsSerializer(produict)
       return JsonResponse(produit_serialize.data)
    
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProduitsSerializer(product_data, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        produit = models.produit.objects.filter(produitId=id)
        print(produit)
        produit.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

class CategorieViewSet(APIView):

   def list_categories(request):
      if request.method == 'GET':
         liste_categories = models.Category.objects.all()
         serialiser_object = CategorieSerializer(liste_categories , many=True)
         return JsonResponse(serialiser_object.data , safe=False)



 

       

 

    
    
 

# Create your views here.
