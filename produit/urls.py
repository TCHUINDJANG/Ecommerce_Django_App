from django.urls import path
from .views import produitViewSet


urlpatterns = [ 
    path('produit/', produitViewSet.as_view()),
    
]