from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from apps.core.models import *

# Create your views here.

def index(request):
    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())
