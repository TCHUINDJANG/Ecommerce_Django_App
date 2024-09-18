from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import produitViewSet , categoryViewSet , commandeViewSet , userViewSet, panierViewSet

router = DefaultRouter()
router.register(r'produit', produitViewSet, basename='produit')
router.register(r'category', categoryViewSet, basename='category')
router.register(r'commande', commandeViewSet, basename='commande')
router.register(r'user', userViewSet, basename='user')
router.register(r'panier', panierViewSet, basename='panier')




urlpatterns = [
    path('', include(router.urls)), 
]