from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from . import models
from rest_framework.decorators import api_view
from . import models
from rest_framework.views import APIView
from rest_framework import status
from . import serialize


#request est une instance de HTTPREQUEST

class produitViewSet(APIView):

    def produit_list_get(request):
     if request.method == 'GET':
        liste_produits = models.produits.objects.all()
        produit_serializer = serialize(liste_produits, many=True)
        return JsonResponse(produit_serializer.data, safe=False)

     elif request.method == 'POST':
        produit_data = JSONParser().parse(request)
        produit_serializer = serialize(data=produit_data)
        if produit_serializer.is_valid():
            produit_serializer.save()
            return JsonResponse("Ajout du produit avec success", status=status.HTTP_201_CREATED) 
        return JsonResponse(produit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
     elif request.method == 'PUT': 
        produit_data = JSONParser().parse(request) 
        produit = models.produit.objects.get(ProduitId=produit_data['ProduitId'])
        produit_serializer = serialize(produit, data=produit_data)
        if produit_serializer.is_valid(): 
            produit_serializer.save() 
            return JsonResponse("Update Successful",safe=False) 
        return JsonResponse(produit_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     elif request.method == 'DELETE': 
        produit = models.produit.objects.filter(produitId=id)
        print(produit)
        produit.delete() 
        return JsonResponse({'message': 'produit was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

    
    
 

# Create your views here.
