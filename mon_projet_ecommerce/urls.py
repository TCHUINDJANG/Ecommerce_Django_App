from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from produit.urls import urlpatterns as produit_url


schema_view = get_schema_view(    #crée une instance de la vue de schéma Swagger
    openapi.Info(                   
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

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(produit_url), name="produit"),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   
# ]
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include(produit_url)),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api.json/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
