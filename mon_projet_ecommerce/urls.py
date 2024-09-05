"""
URL configuration for mon_projet_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
#from .views import CategorieViewSet, ProduitViewSet, PanierViewSet, ArticleDuPanierViewSet, CommandeViewSet, DetailCommandeViewSet, AvisViewSet, TransactionViewSet, ExpeditionViewSet



router = DefaultRouter()
#router.register(r'categories', CategorieViewSet)
#router.register(r'produits', ProduitViewSet)
#router.register(r'paniers', PanierViewSet)
#router.register(r'articles-du-panier', ArticleDuPanierViewSet)
#router.register(r'commandes', CommandeViewSet)
#router.register(r'details-commandes', DetailCommandeViewSet)
#router.register(r'avis', AvisViewSet)
#router.register(r'transactions', TransactionViewSet)
#router.register(r'expeditions', ExpeditionViewSet)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produit.urls'), name="produit"),

   # path('', include(router.urls)),
    
]


#endpoint = 'http://127.0.0.1/api/produit/'
