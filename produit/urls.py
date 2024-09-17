from django.urls import path
from .views import produitViewSet
from rest_framework.routers import DefaultRouter





urlpatterns = [ 
    path('produit/', produitViewSet.as_view()),
    
]

router = DefaultRouter()
router.register(r'produit', produitViewSet, basename='produit')
# urlpatterns = router.urls
