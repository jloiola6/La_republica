from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from apps.usuario.components import verification
from apps.core.models import *


# Create your views here.

def index(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        
    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())
