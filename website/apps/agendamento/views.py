from django.contrib.auth.decorators import login_required

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from datetime import datetime

from apps.agendamento.models import *
from apps.agendamento.components import consultar_horarios, consultar_servico, verificar_colaborador
from apps.agendamento.action import *
from apps.usuario.models import *


# Create your views here.

@login_required(login_url='/usuario/login')
def index(request):
    usuario = request.user
    
    template_name = 'agendamento/index.html'

    servicos = Servico.objects.all()

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def agendamento_horario(request, servico_id):
    usuario = request.user
    
    template_name = 'agendamento/horario.html'

    servico = Servico.objects.get(id= servico_id)
    grades = consultar_horarios(servico)

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def agendamento_concluir(request, servico_id, data, hora):
    usuario = request.user
    servico = Servico.objects.get(id= servico_id)
    data = datetime.strptime(data, '%Y-%m-%d').date()

    if not consultar_servico(servico, data, hora= hora):
        return HttpResponseRedirect('/')
    
    template_name = 'agendamento/concluir.html'
    
    preco = PrecoServico.objects.get(servico= servico, situacao= 1)
    colaboradores = verificar_colaborador(preco, data, hora)

    if request.method == 'POST':
        agendamento(request, usuario, preco, data, hora)
    
    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def cadastrar_servico(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/formulario-servico.html'

    if request.method == 'POST':
        servico_cadastro(request)

        return HttpResponseRedirect('/agendamento/listar-servicos')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def editar_servico(request, servico_id):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/formulario-servico.html'

    servico = Servico.objects.get(id= servico_id)
    preco = PrecoServico.objects.filter(servico= servico_id).last()

    if request.method == 'POST':
        servico_cadastro(request, servico)

        return HttpResponseRedirect('/agendamento/listar-servicos')

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def listar_servico(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/servicos.html'

    servicos = Servico.objects.all()

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def perfil_servico(request, servico_id):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/servico-perfil.html'

    servico = Servico.objects.get(id= servico_id)
    precos = PrecoServico.objects.filter(servico= servico)
    colaboradores = ColaboradorServico.objects.filter(servico= servico)

    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def servico_colaborador(request, servico_id):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/associar-colaborador.html'

    
    servicos = Servico.objects.filter(id= servico_id)
    colaboradores_existente = ColaboradorServico.objects.filter(servico= servicos.last()).values_list('colaborador__id', flat= True).distinct()
    colaboradores = Colaborador.objects.exclude(id__in= colaboradores_existente)

    if request.method == 'POST':
        colaborador_servico_associar(request, servicos.last())

        return HttpResponseRedirect('/usuario/menu-perfil')

    return TemplateResponse(request, template_name, locals())


