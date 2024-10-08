from rest_framework import routers
from django.urls import path, include
from . import views
# from .views import UserViewSet

router = routers.DefaultRouter()
# router.register(r'', views.UserViewSet)
# router.register(r'', UserViewSet)


urlpatterns = [
    path("register/", views.RegistrationView, name="register"),
    path("confirm-registration/", views.ConfirmRegistration, name="confirm_registration"),
    # path('login/', UserViewSet.as_view({'post': 'login_view'}), name='login'),
    # path('logout/', UserViewSet.as_view({'post': 'logout_view'}), name='logout'),
    # path('forgot-password/', UserViewSet.as_view({'post': 'forgot_password_view'}), name='forgot_password'),
    path('', include(router.urls)),
]