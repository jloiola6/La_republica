from django.urls import path

from apps.clube.views import *

app_name = 'clube'

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    # path('checkout/', checkout, name='checkout'),
    # path('finalizado/', finalizado, name='finalizado'),
    path("cancelar-assinatura", cancelar_assinatura, name="cancelar-assinatura"), #add this
]