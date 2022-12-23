from django.urls import path

from apps.agendamento.views import *

app_name = 'agendamento'

urlpatterns = [
    path('cadastrar-servico', cadastrar_servico, name='cadastrar-servico'),
    path('editar-servico/<int:servico_id>', editar_servico, name='editar-servico'),
    path('listar-servicos', listar_servico, name='listar-servicos'),
    path('perfil-servico/<int:servico_id>', perfil_servico, name='perfil-servico'),
    path('servico-colaborador/<int:servico_id>', servico_colaborador, name='servico-colaborador'),
]