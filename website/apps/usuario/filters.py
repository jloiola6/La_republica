from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
import stripe

from apps.usuario.components import verificador_vazio
from apps.usuario.models import *


def filtros_usuarios(request):
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')

    usuarios = User.objects.exclude(is_superuser= 1)
    if not verificador_vazio(tipo):
        if tipo == 'C':
            colaborador_id = Colaborador.objects.values_list('usuario__id', flat= True)
            usuarios = usuarios.filter(id__in= colaborador_id)

        elif tipo == 'A':
            usuarios = usuarios.filter(clube= 1)

        elif tipo == 'Adm':
            adm_id = Adm.objects.values_list('usuario__id', flat= True)
            usuarios = usuarios.filter(id__in= adm_id)

    if not verificador_vazio(nome):
        usuarios = usuarios.filter(username__contains= nome)

    return usuarios