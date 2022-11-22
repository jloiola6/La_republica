from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from apps.usuario.models import *

# Create your views here.

def login(request):
    template_name = 'usuario/login.html'

    return TemplateResponse(request, template_name, locals())
