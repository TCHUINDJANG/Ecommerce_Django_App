from django.conf import settings
from django.contrib import admin
from django.urls import path, include     # importer ce fichier pour la video
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from produit.urls import urlpatterns as produit_url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,                #classe permettant d'avoir le token
    TokenRefreshView,    #classe permettant de refresh le tken                 
    TokenVerifyView              #classe permettant de verifier le token
)

schema_view = get_schema_view(    #crée une instance de la vue de schéma Swagger
    openapi.Info(                   
        title="Mon Application de Ecommerce",
        default_version='v1.0',
        description="Description de mon API de Ecommerce",
        terms_of_service="https://www.google.com/policies/terms/",  
        contact=openapi.Contact(email="contact@monapi.local"),   
        license=openapi.License(name="BSD License"),       
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),  #ajouter ceci
    path('account/', include('users.urls')),  #ajouter ceci
    path("api/", include(produit_url)),    #ajouter ceci

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api.json/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
