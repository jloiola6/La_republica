from django.urls import path

from apps.clube.views import *

app_name = 'clube'

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('criar-assinatura/', criar_assinatura, name='checkout'),
    path("cancelar-assinatura", cancelar_assinatura, name="cancelar-assinatura"),
]