from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from djstripe.models import Product

from apps.usuario.views import verification
from apps.usuario.models import Usuario
from apps.core.models import *


# Create your views here.

def index(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])
        
    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())
