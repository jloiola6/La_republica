from apps.usuario.models import Usuario

def cadastrar_usuario(nome, user, password):
    usuario = None
    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if 10 > len(user) < 50 and '@' in user and '.' in user:
        campos_invalidos.append('Email')

    if 15 > len(password) < 150:
        campos_invalidos.append('Password')

    if not Usuario.objects.filter(email= user, senha= password).exists() and campos_invalidos == []:
        usuario = Usuario()
        usuario.nome = nome
        usuario.email = user
        usuario.senha = password
        usuario.save()
    
    return usuario, campos_invalidos