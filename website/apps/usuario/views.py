from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from apps.agendamento.models import *
from apps.usuario.models import *
from apps.usuario.action import *
from apps.usuario.filters import *
from apps.usuario.components import verification
from apps.clube.components import *

# Create your views here.admin   


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass

    return HttpResponseRedirect('/usuario/login')


def login(request):
    if verification(request):
        return HttpResponseRedirect('/')

    template_name = 'usuario/login.html'
    
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')

        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        
        if User.objects.filter(email= user, password= password).exists():
            usuario = User.objects.get(email= user, password= password)
            request.session['id'] = usuario.id
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


def cadastro(request):
    if verification(request):
        return HttpResponseRedirect('/')
        
    template_name = 'usuario/cadastro.html'

    if request.method == 'POST':
        usuario, campos_invalidos = cadastrar_usuario(request)

        if usuario:
            request.session['id'] = usuario.id
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'usuario/resetar-senha.html'
    email_template_name = 'usuario/resetar-senha-email.html'
    subject_template_name = 'usuario/resetar-senha-assunto.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('usuario:login')


def perfil(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])

    template_name = 'usuario/perfil.html'

    return TemplateResponse(request, template_name, locals())


def associar_colaborador(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/associar-colaborador.html'

    colabores = Colaborador.objects.values_list('usuario__id', flat= True)
    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = User.objects.exclude(id__in= colabores).exclude(id__in= adms)

    if request.method == 'POST':
        colaborador_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


def servico_colaborador(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/servico-colaborador.html'

    colaboradores = Colaborador.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        colaborador_servico_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


def associar_adm(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/associar-adm.html'

    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = User.objects.exclude(id__in= adms).exclude(is_superuser= 1)

    if request.method == 'POST':
        adm_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


def usuarios(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/usuarios.html'

    usuarios = filtros_usuarios(request)

    return TemplateResponse(request, template_name, locals())
