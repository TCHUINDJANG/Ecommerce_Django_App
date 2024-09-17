from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import produitViewSet

router = DefaultRouter()
router.register(r'produit', produitViewSet, basename='produit')

urlpatterns = [
    path('', include(router.urls)), 
]