from rest_framework import serializers
from .models import produits


class ProduitsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = produits
        fields =('ProduitId','produitname','photoName','stock','image')