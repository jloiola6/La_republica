from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
import stripe

from apps.usuario.components import verificador_vazio
from apps.usuario.models import *


def filtros_usuarios(request):
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')

    usuarios = User.objects.all()
    print(usuarios)
    if not verificador_vazio(tipo):
        if tipo == 'C':
            usuarios = Colaborador.objects.all()

        elif tipo == 'A':
            usuarios = usuarios.filter(clube= 1)

            # emails = []
            # stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

            # print(stripe.Subscription.retrieve("sub_1MGwQgGORsxenfcwFy6BRt39"))
            # subs = stripe.Subscription.search(query="status:'active'")['data']

            # if subs != []:
            #     customers = []
            #     for sub in subs:
            #         customers.append(sub['customer'])

            # if customers != []:
            #     for customer in customers:
            #         emails.append(stripe.Customer.retrieve(customer)['email'])

            # if emails != []:
            #     usuarios = usuarios.filter(email__in= emails)

        elif tipo == 'Adm':
            usuarios = Adm.objects.all()

    if not verificador_vazio(nome):
        usuarios = usuarios.filter(username__contains= nome)

    return usuarios