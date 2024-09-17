from django.conf import settings
from django.urls import path
from .views import produitViewSet
from rest_framework.routers import DefaultRouter



from rest_framework.routers import DefaultRouter, SimpleRouter

# router = None
# if settings.DEBUG:
#     router = DefaultRouter()
# else:
#     router = SimpleRouter()

# router.register(r'produit', produitViewSet.produit_list_get, basename='produit')

    
# urlpatterns = router.urls



urlpatterns = [ 
    path('produit/', produitViewSet.produit_list_get),
    
]


# urlpatterns = router.urls

# router = DefaultRouter()
# router.register(r'produit', produitViewSet, basename='produit')
# urlpatterns = router.urls
