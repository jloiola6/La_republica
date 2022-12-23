from django.urls import path

from apps.agendamento.views import *

app_name = 'agendamento'

urlpatterns = [
    path('cadastrar-servico', cadastrar_servico, name='cadastrar-servico'),
]