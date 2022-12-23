from django.contrib.auth.decorators import login_required

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.agendamento.models import *
from apps.agendamento.action import *
from apps.usuario.models import *


# Create your views here.

@login_required(login_url='/usuario/login')
def cadastrar_servico(request):
    usuario = request.user
    if not Adm.objects.filter(usuario= usuario).exists():
        return HttpResponseRedirect('/')

    template_name = 'agendamento/cadastrar-servico.html'

    if request.method == 'POST':
        servico_cadastro(request)

        return HttpResponseRedirect('/')

    return TemplateResponse(request, template_name, locals())


