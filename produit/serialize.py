from rest_framework import serializers
from .models import produits, Category, User , Panier, ArticlesDuPanier, Commande, DetailsCommandes, Avis, Transaction, Expedition



class ProduitsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = produits
        fields =('titre','prix','description','category','image' , 'date_ajout', 'stock')

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = '__all__'


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'

class ArticleDuPanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesDuPanier
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class DetailCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsCommandes
        fields = '__all__'

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'