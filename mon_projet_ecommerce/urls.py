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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter


#from .views import CategorieViewSet, ProduitViewSet, PanierViewSet, ArticleDuPanierViewSet, CommandeViewSet, DetailCommandeViewSet, AvisViewSet, TransactionViewSet, ExpeditionViewSet




#router.register(r'categories', CategorieViewSet)
#router.register(r'produits', ProduitViewSet)
#router.register(r'paniers', PanierViewSet)
#router.register(r'articles-du-panier', ArticleDuPanierViewSet)
#router.register(r'commandes', CommandeViewSet)
#router.register(r'details-commandes', DetailCommandeViewSet)
#router.register(r'avis', AvisViewSet)
#router.register(r'transactions', TransactionViewSet)
#router.register(r'expeditions', ExpeditionViewSet)



schema_view = get_schema_view(    #crée une instance de la vue de schéma Swagger
    openapi.Info(                   #est un objet qui contient les informations de base sur l'API
        title="Mon Application de Ecommerce",
        default_version='v1.0',
        description="Description de mon API de Ecommerce    ",
        terms_of_service="https://www.google.com/policies/terms/",   #Lien vers les termes et conditions d'utilisation de l'API
        contact=openapi.Contact(email="contact@monapi.local"),   #Fournit les informations de contact pour l'API
        license=openapi.License(name="BSD License"),       #Spécifie les informations sur la licence de l'API
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# http://127.0.0.1:8000/swagger/



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produit.urls'), name="produit"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


   # path('', include(router.urls)),
    
]


#endpoint = 'http://127.0.0.1/api/produit/'
