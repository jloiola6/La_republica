from apps.usuario.models import Usuario

def cadastrar_usuario(nome, user, password):
    if not Usuario.objects.filter(email= user, senha= password).exists():
        usuario = Usuario()
        usuario.nome = nome
        usuario.email = user
        usuario.senha = password
        usuario.save()
    
    return usuario