from django.urls import path

from apps.agendamento.views import *

app_name = 'agendamento'

urlpatterns = [
    path('', index, name='index'),
    path('horario/<int:servico_id>', agendamento_horario, name='horario'),
    path('concluir/<int:servico_id>/<str:data>/<str:hora>', agendamento_concluir, name='concluir'),
    path('cadastrar-servico', cadastrar_servico, name='cadastrar-servico'),
    path('editar-servico/<int:servico_id>', editar_servico, name='editar-servico'),
    path('listar-servicos', listar_servico, name='listar-servicos'),
    path('perfil-servico/<int:servico_id>', perfil_servico, name='perfil-servico'),
    path('servico-colaborador/<int:servico_id>', servico_colaborador, name='servico-colaborador'),
]