from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from apps.usuario.components import verification
from apps.core.models import *


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        usuario = request.user
        
    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())
