from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.agendamento.models import *
from apps.usuario.models import *
from apps.usuario.action import *
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
        usuario, campos_invalidos = cadastrar_usuario(request)

        if usuario:
            request.session['id'] = usuario.id
            return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


def perfil(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])

    template_name = 'usuario/perfil.html'

    return TemplateResponse(request, template_name, locals())


def associar_colaborador(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/associar_colaborador.html'

    colabores = Colaborador.objects.values_list('usuario__id', flat= True)
    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = Usuario.objects.exclude(id__in= colabores).exclude(id__in= adms)

    if request.method == 'POST':
        colaborador_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


def servico_colaborador(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/servico_colaborador.html'

    colaboradores = Colaborador.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        colaborador_servico_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())


def associar_adm(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])
        if not Adm.objects.filter(usuario= usuario).exists():
            return HttpResponseRedirect('/')

    template_name = 'usuario/associar_adm.html'

    adms = Adm.objects.values_list('usuario__id', flat= True)
    usuarios = Usuario.objects.exclude(id__in= adms)

    if request.method == 'POST':
        adm_associar(request)

        return HttpResponseRedirect('/usuario/perfil')

    return TemplateResponse(request, template_name, locals())
