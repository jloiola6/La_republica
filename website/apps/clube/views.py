from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.conf import settings

import stripe
import json


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        usuario = request.user
        if usuario.clube == 1:
            return HttpResponseRedirect('/clube/perfil')

    template_name = 'clube/index.html'

    produtos = []
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    for plan in stripe.Plan.list():
        plano_id = plan['id']
        produto_id = plan['product']
        product = stripe.Product.retrieve(produto_id)
        valor = plan['amount_decimal']
        valor = f'{valor[:len(valor)-2]},{valor[-2:]}'        
        
        produtos.append({'plano_id': plano_id,
                'produto_id': produto_id,
                'name': product['name'],
                'description': product['description'],
                'valor': valor})
    
    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def perfil(request):
    template_name = 'clube/perfil.html'

    usuario = request.user
    clube = usuario.clube == 1
    
    return TemplateResponse(request, template_name, locals())


@login_required(login_url='/usuario/login')
def cancelar_assinatura(request):
    usuario = request.user
    sub = usuario.id_subscription

    try:
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        stripe.Subscription.delete(sub)

        request.user.clube = 0
        request.user.save()
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status =403)

    return HttpResponseRedirect('/')


@login_required
def criar_assinatura(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        try:
            #Criando usuário
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )

            #Criando Assinatura
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )

            #Vinculando assinatura criada ao usuário do sistema
            request.user.id_consumer = customer.id
            request.user.id_subscription = subscription.id
            request.user.clube = 1
            request.user.save()

            return JsonResponse(subscription)

        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status =403)
    else:
        print('requet method not allowed')