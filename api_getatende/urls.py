from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/painel/')),
    path('painel', admin.site.urls),
    path('maquina-obsoleta/', include('maquina_obsoleta.urls'), name='maquina_obsoleta'),
    path('ecommerce/', include('ecommerce.urls'), name='e-commerce'),
]
