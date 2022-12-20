
def verification(request):
    try:
        if request.session['id']:
            return True
    except KeyError:
        return False

def verificador_vazio(atributo):
    return atributo in ('', None)