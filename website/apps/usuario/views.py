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


def menu_perfil(request):
    if request.user.is_authenticated:
        usuario = request.user

    template_name = 'usuario/perfil.html'

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def associar_colaborador(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/associar-colaborador.html'

    colabores = Colaborador.objects.values_list('usuario__id', flat= True)
    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = User.objects.exclude(id__in= colabores).exclude(id__in= adms).exclude(is_superuser= 1)

    if request.method == 'POST':
        colaborador_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def servico_colaborador(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/servico-colaborador.html'

    colaboradores = Colaborador.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        colaborador_servico_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def associar_adm(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/associar-adm.html'

    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = User.objects.exclude(id__in= adms).exclude(is_superuser= 1)

    if request.method == 'POST':
        adm_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def usuarios(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'usuario/usuarios.html'

    usuarios = filtros_usuarios(request)

    return TemplateResponse(request, template_name, locals())

