import hashlib

from apps.usuario.models import *
from apps.agendamento.models import *

def cadastrar_usuario(request):
    nome = request.POST.get('nome')
    user = request.POST.get('user')
    password = request.POST.get('password')

    password = hashlib.md5(password.encode())
    password = password.hexdigest()

    usuario = None
    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if 10 > len(user) < 50 and '@' in user and '.' in user:
        campos_invalidos.append('Email')

    if 15 > len(password) < 150:
        campos_invalidos.append('Password')

    if not Usuario.objects.filter(email= user, senha= password).exists() and campos_invalidos == []:
        usuario = Usuario()
        usuario.nome = nome
        usuario.email = user
        usuario.senha = password
        usuario.save()
    
    return usuario, campos_invalidos


def colaborador_associar(request):
    colaborador = request.POST.get('colaborador')

    if Usuario.objects.filter(id= colaborador).exists():
        usuario = Usuario.objects.get(id= colaborador)
        
        if not Colaborador.objects.filter(usuario= usuario).exists():
            colaborador = Colaborador()
            colaborador.usuario = usuario
            colaborador.save()


def colaborador_servico_associar(request):
    colaborador = request.POST.get('colaborador')
    servico = request.POST.get('servico')

    if Colaborador.objects.filter(id= colaborador).exists() and Servico.objects.filter(id= servico).exists():
        colaborador = Colaborador.objects.get(id= colaborador)
        servico = Servico.objects.get(id= servico)

        if not ColaboradorServico.objects.filter(colaborador= colaborador, servico= servico).exists():
            colaborador_servico = ColaboradorServico()
            colaborador_servico.colaborador = colaborador
            colaborador_servico.servico = servico
            colaborador_servico.save()