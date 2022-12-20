from django.urls import path

from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('cadastro', cadastro, name='cadastro'),
    path('perfil', perfil, name='perfil'),
    path('associar-colaborador', associar_colaborador, name='associar-colaborador'),
    path('servico-colaborador', servico_colaborador, name='servico-colaborador'),
]