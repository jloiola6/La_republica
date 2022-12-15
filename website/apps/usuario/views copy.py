from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from apps.usuario.models import *

# Create your views here.admin

def verification(request):
    try:
        if request.session['id']:
            return True
    except KeyError:
        return False


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

        if Usuario.objects.filter(email= user, senha= password).exists():
            usuario = Usuario.objects.get(email= user, senha= password)
            request.session['id'] = usuario.id
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())

def cadastro(request):
    template_name = 'usuario/cadastro.html'

    return TemplateResponse(request, template_name, locals())
