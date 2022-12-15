from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
import hashlib

from apps.usuario.models import *
from apps.usuario.action import cadastrar_usuario
from apps.usuario.components import verification
from apps.clube.components import *

# Create your views here.admin   

def login(request):
    if verification(request):
        return HttpResponseRedirect('/')

    template_name = 'usuario/login.html'
    
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')

        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        
        if Usuario.objects.filter(email= user, senha= password).exists():
            usuario = Usuario.objects.get(email= user, senha= password)
            request.session['id'] = usuario.id
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


def cadastro(request):
    if verification(request):
        return HttpResponseRedirect('/')
        
    template_name = 'usuario/cadastro.html'

    if request.method == 'POST':
        nome = request.POST.get('nome')
        user = request.POST.get('user')
        password = request.POST.get('password')

        password = hashlib.md5(password.encode())
        password = password.hexdigest()

        usuario = cadastrar_usuario(nome, user, password)

        request.session['id'] = usuario.id

        return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass

    return HttpResponseRedirect('/usuario/login')

def perfil(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])

    template_name = 'usuario/perfil.html'

    return TemplateResponse(request, template_name, locals())