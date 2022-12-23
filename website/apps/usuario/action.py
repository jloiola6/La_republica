# from django.contrib.auth.models import User
from apps.usuario.models import User


def cadastrar_usuario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    # password = hashlib.md5(password.encode())
    # password = password.hexdigest()

    usuario = None
    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if 10 > len(email) < 50 and '@' in email and '.' in email:
        campos_invalidos.append('Email')

    if 15 > len(password) < 150:
        campos_invalidos.append('Password')
    
    if not User.objects.filter(email= email, password= password).exists():
        usuario = User.objects.create_user(
            username= email,
            first_name = nome,
            email = email,
            password = password
        )
        usuario.save()
    
    return usuario, campos_invalidos


def colaborador_associar(request):
    colaborador = request.POST.get('colaborador')

    if Usuario.objects.filter(id= colaborador).exists():
        usuario = Usuario.objects.get(id= colaborador)
        
        if not Colaborador.objects.filter(usuario= usuario).exists():
            colaborador = Colaborador()
            colaborador.usuario = usuario
            colaborador.save()


def colaborador_servico_associar(request):
    colaborador = request.POST.get('colaborador')
    servico = request.POST.get('servico')

    if Colaborador.objects.filter(id= colaborador).exists() and Servico.objects.filter(id= servico).exists():
        colaborador = Colaborador.objects.get(id= colaborador)
        servico = Servico.objects.get(id= servico)

        if not ColaboradorServico.objects.filter(colaborador= colaborador, servico= servico).exists():
            colaborador_servico = ColaboradorServico()
            colaborador_servico.colaborador = colaborador
            colaborador_servico.servico = servico
            colaborador_servico.save()


def adm_associar(request):
    usuario = request.POST.get('usuario')

    if Usuario.objects.filter(id= usuario).exists():
        usuario = Usuario.objects.get(id= usuario)
        
        if not Adm.objects.filter(usuario= usuario).exists():
            adm = Adm()
            adm.usuario = usuario
            adm.save()