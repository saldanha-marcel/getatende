from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('maquina-obsoleta/', include('maquina_obsoleta.urls'), name='maquina_obsoleta'),
    path('ecommerce/', include('ecommerce.urls'), name='e-commerce'),
]
