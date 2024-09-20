 
from django.urls import path, include
from . import views



path('generate-token/<str:id>/<str:token>/', views.generate_token, name='generate-token'),
path('process-payment/<str:id>/<str:token>/', views.process_payment, name='process-payment'),
