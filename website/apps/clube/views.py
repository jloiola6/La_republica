from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
# from djstripe.models.api import APIKey
from django.http import JsonResponse
from http.client import HTTPResponse
# from djstripe.models import Product
from django.conf import settings
# import djstripe
import stripe
import json

from apps.usuario.views import verification
from apps.usuario.models import Usuario
from apps.clube.models import LinkPagamento


# Create your views here.

def index(request):
    if verification(request):
        usuario = Usuario.objects.get(id= request.session['id'])

    template_name = 'clube/index.html'

    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    produtos = []
    for product in  stripe.Product.list():
        for plan in stripe.Plan.list():
            if plan['product'] == product['id']:
                valor = plan['amount_decimal']
                valor = f'{valor[:len(valor)-2]},{valor[-2:]}'
                break
        
        link = LinkPagamento.objects.get(produto= product['id']).link
        produtos.append({'name': product['name'],
                'description': product['description'],
                'valor': valor,
                'link': link})

    
    # links = LinkPagamento.objects.all()

    # chave = settings.STRIPE_TEST_SECRET_KEY

    # stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    # valores = stripe.Customer.search(
    #     query="email:'jloiola6@outoook.com' or phone:'+55 68 99902 1108'",
    # )

    return TemplateResponse(request, template_name, locals())


# def checkout(request):
#     if not verification(request):
#         return HttpResponseRedirect('/')

#     usuario = Usuario.objects.get(id= request.session['id'])
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