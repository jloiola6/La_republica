from django.conf import settings
import stripe


def usuario_stripe(usuario):
    try:
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        stripe_id = stripe.Customer.search(query=f"email: '{usuario.email}'")['data'][0]['id']

        return stripe_id
    except:
        print('Erro ao sincronizar dados do usuário id: ', usuario.id)
        return None
        

def verificando_assinatura(usuario):
    stripe_id = usuario_stripe(usuario)
    if stripe_id is not None:
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

        sub = list(stripe.Invoice.search(query=f"customer: '{stripe_id}'"))[-1]['subscription']
        if stripe.Subscription.retrieve(sub)['status'] == 'active':
            return True
    
    return False
