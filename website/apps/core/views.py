from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.core.models import *


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        usuario = request.user
        
    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())
