from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import stripe

from apps.usuario.components import verification
from apps.clube.models import LinkPagamento
from apps.clube.components import *


# Create your views here.

def index(request):
    if verification(request):
        usuario = User.objects.get(id= request.session['id'])
        if verificando_assinatura(usuario):
            return HttpResponseRedirect('/clube/perfil')

    template_name = 'clube/index.html'

    produtos = []
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    for plan in stripe.Plan.list():
        product = stripe.Product.retrieve(plan['product'])
        valor = plan['amount_decimal']
        valor = f'{valor[:len(valor)-2]},{valor[-2:]}'        
        link = LinkPagamento.objects.get(produto= product['id']).link
        
        produtos.append({'name': product['name'],
                'description': product['description'],
                'valor': valor,
                'link': link})
    
    return TemplateResponse(request, template_name, locals())


def perfil(request):
    if not verification(request):
        return HttpResponseRedirect('/')

    template_name = 'clube/perfil.html'

    usuario = User.objects.get(id= request.session['id'])
    clube = verificando_assinatura(usuario)
    
    return TemplateResponse(request, template_name, locals())


def cancelar_assinatura(request):
    if not verification(request):
        return HttpResponseRedirect('/')
    
    usuario = User.objects.get(id= request.session['id'])
    stripe_id = usuario_stripe(usuario)

    sub = list(stripe.Invoice.search(query=f"customer: '{stripe_id}'"))
    sub = sub[-1]['subscription']

    try:
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        stripe.Subscription.delete(sub)
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status =403)

    return HttpResponseRedirect('/')


# def checkout(request):
#     if not verification(request):
#         return HttpResponseRedirect('/')

#     usuario = User.objects.get(id= request.session['id'])
#     print('0')
#     if request.method == 'POST':
#         # Reads application/json and returns a response
#         data = json.loads(request.body)
#         payment_method = data['payment_method']
#         print('Método: ', payment_method)
#         # stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY
#         stripe.api_key = 'sk_test_51M77STGORsxenfcwIpIsRrkxKv8cVgpzjmk3bVRcATWjRCFFKQxRpqgXoeSJOKeU0DTJPbxzOTfRLxR70zRcEtoe00PcCkVNWc'
        

#         #Criando Método de pagamentos
#         metodo = stripe.PaymentMethod.create(
#                 type="card",
#                 card={
#                     "number": "4242424242424242",
#                     "exp_month": 12,
#                     "exp_year": 2034,
#                     "cvc": "123",
#                 },
#         )

#         print(metodo)

#         payment_method_obj = stripe.PaymentMethod.retrieve(payment_method, )
#         print('Saida: ', payment_method_obj)

#         # payment_method_obj = stripe.PaymentMethod.retrieve()
#         print('Método 2: ', payment_method_obj)
#         print('teste de teste')
#         djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

#         print('1')

#         try:
#             inscricao = InscricaoClube()
#             # This creates a new Customer and attaches the PaymentMethod in one API call.
#             customer = stripe.Customer.create(
#                 payment_method = payment_method,
#                 email = usuario.email,
#                 invoice_settings = {
#                     'default_payment_method': payment_method
#                 }
#             )

#             djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
#             inscricao.customer = djstripe_customer
            
#             print('2')

#             # At this point, associate the ID of the Customer object with your
#             # own internal representation of a customer, if you have one.
#             # print(customer)

#             # Subscribe the user to the subscription created
#             subscription = stripe.Subscription.create(
#                 customer=customer.id,
#                 items=[
#                     {
#                         "price": data["price_id"],
#                     },
#                 ],
#                 expand=["latest_invoice.payment_intent"]
#             )
#             print('3')

#             djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

#             inscricao.subscription = djstripe_subscription
#             inscricao.save()

#             print('4')
#             return JsonResponse(subscription)
#         except Exception as e:
#             print('5')
#             return JsonResponse({'error': (e.args[0])}, status =403)
#     else:
#         print('6')
#         return HTTPResponse('requet method not allowed')


# def finalizado(request):
#     template_name = 'clube/finalizado.html'

#     return TemplateResponse(request, template_name, locals())