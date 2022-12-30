# from django.contrib.auth.models import User
from apps.usuario.models import *
from apps.agendamento.models import ColaboradorServico, Servico


def cadastrar_usuario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    password = request.POST.get('password')

    usuario = None
    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if 10 > len(email) < 50 and '@' in email and '.' in email:
        campos_invalidos.append('Email')

    if 15 > len(password) < 150:
        campos_invalidos.append('Password')
    
    if not User.objects.filter(email= email, password= password).exists():
        usuario = User.objects.create_user(
            username= email,
            first_name = nome,
            email = email,
            password = password
        )
        usuario.save()
    
    return usuario, campos_invalidos


def editar_usuario(request, usuario):
    nome = request.POST.get('nome')

    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if campos_invalidos == []:
        usuario.first_name = nome
        usuario.save()
    
    return campos_invalidos


def colaborador_associar(request, perfil_id):
    if User.objects.filter(id= perfil_id).exists():
        usuario = User.objects.get(id= perfil_id)
        
        if not Colaborador.objects.filter(usuario= usuario).exists():
            colaborador = Colaborador()
            colaborador.usuario = usuario
            colaborador.save()


def adm_associar(request, perfil_id):
    if User.objects.filter(id= perfil_id).exists():
        usuario = User.objects.get(id= perfil_id)
        
        if not Adm.objects.filter(usuario= usuario).exists():
            adm = Adm()
            adm.usuario = usuario
            adm.save()