from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('cnpj/', views.get_or_create_cnpj, name='create_cnpj'),
    path('cnpj/<str:number_cnpj>/',  views.get_or_create_cnpj, name='get_by_number_cnpj'),
    path('multicnpj/', views.create_multiple_cnpjs, name='create_multiple_cnpjs'),
]
