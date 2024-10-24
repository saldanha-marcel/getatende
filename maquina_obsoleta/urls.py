from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('serial/', views.get_or_create_serial, name='create_serial'),
    path('serial/<str:number_serial>/',  views.get_or_create_serial, name='get_by_number_serial'),
    path('multiserial/', views.create_multiple_serials, name='create_multiple_serials'),
]
