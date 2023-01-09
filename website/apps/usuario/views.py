from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.usuario.filters import *
from apps.usuario.action import *
from apps.agendamento.models import *
from apps.usuario.models import *

# Create your views here.

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'usuario/resetar-senha/resetar-senha.html'
    email_template_name = 'usuario/resetar-senha/email-texto.html'
    subject_template_name = 'usuario/resetar-senha/email-assunto.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('usuario:login')


def logout(request):
    logout_django(request)
    return HttpResponseRedirect('/usuario/login')


def cadastro(request):
    template_name = 'usuario/cadastro.html'

    if request.method == 'POST':
        usuario, campos_invalidos = cadastrar_usuario(request)

        if usuario:
            login_django(request, usuario)
            return HttpResponseRedirect('/')
        else:
            print(campos_invalidos)

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def editar_dados(request, perfil_id):
    usuario = request.user
    perfil = User.objects.get(id= perfil_id)
    if usuario.id != perfil_id and not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/cadastrogit.html'

    if request.method == 'POST':
        campos_invalidos = editar_usuario(request, perfil)
        
        if campos_invalidos == []:
            return HttpResponseRedirect('/')
        else:
            print(campos_invalidos)

    return TemplateResponse(request, template_name, locals())


def login(request):
    template_name = 'usuario/login.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        usuario = authenticate(username= email, password= password)
        if usuario:
            login_django(request, usuario)
            return HttpResponseRedirect('/')
        else:
            erro = 'Email ou senha inválido'

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def perfil(request, perfil_id):
    usuario = request.user
    perfil = User.objects.get(id= perfil_id)
    if usuario.id != perfil_id and not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/perfil.html'

    usuario_adm = Adm.objects.filter(usuario__id= usuario.id).exists()
    adm = Adm.objects.filter(usuario__id= perfil_id).exists()
    colaborador = Colaborador.objects.filter(usuario__id= perfil_id).exists()

    if request.method == 'POST':
        if request.POST.get('associar_colaborador'):
            colaborador_associar(request, perfil_id)
        elif request.POST.get('associar_adm'):
            adm_associar(request, perfil_id)
        
        return HttpResponseRedirect(f'/usuario/perfil/{perfil_id}')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def menu_perfil(request):
    usuario = request.user

    print(usuario)
    print(usuario.first_name)
    print(usuario.email)

    template_name = 'usuario/menu-perfil.html'

    agendamentos = Agendamento.objects.filter(cliente= usuario, situacao= 'Reservado')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def usuarios(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/usuarios.html'

    usuarios = filtros_usuarios(request)

    return TemplateResponse(request, template_name, locals())

