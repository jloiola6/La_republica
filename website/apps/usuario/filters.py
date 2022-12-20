from django.conf import settings
import stripe

from apps.usuario.components import verificador_vazio
from apps.usuario.models import *


def filtros_usuarios(request):
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')

    
    usuarios = Usuario.objects.all()
    if not verificador_vazio(tipo):
        if tipo == 'C':
            usuarios = Colaborador.objects.all()

        elif tipo == 'A':
            emails = []
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
            subs = stripe.Subscription.search(query="status:'active'")['data']

            if subs != []:
                customers = []
                for sub in subs:
                    customers.append(sub['customer'])

            if customers != []:
                for customer in customers:
                    emails.append(stripe.Customer.retrieve(customer)['email'])

            if emails != []:
                usuarios = usuarios.filter(email__in= emails)

        elif tipo == 'Adm':
            usuarios = Adm.objects.all()

    if not verificador_vazio(nome):
        usuarios = usuarios.filter(nome__contains= nome)

    return usuarios