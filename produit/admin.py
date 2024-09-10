from django.contrib import admin
from .models import Category, produits , Panier , Commentaire



class AdminCategory(admin.ModelAdmin):

    list_display = ('name','date_ajout')

class AdminProduct(admin.ModelAdmin):

    list_display = ('titre','prix', 'category','date_ajout')


class AdminPanier(admin.ModelAdmin):
    list_display = ('utilisateur','date_creation_commande','ordered')

class AdminCommentaire(admin.ModelAdmin):
    list_display = ('date_commentaire','statut')

# Register your models here.
admin.site.register(produits , AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Panier , AdminPanier)
admin.site.register(Commentaire , AdminCommentaire)
