
def verification(request):
    try:
        if request.session['id']:
            return True
    except KeyError:
        return False

