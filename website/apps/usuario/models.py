from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Adm(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    dt_entrada = models.DateField(auto_now_add=True)
    dt_saida = models.DateField(null= True, blank= True)
    situacao = models.IntegerField(default= 1)

    def __str__(self):
        return self.usuario.nome


class Colaborador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.DO_NOTHING)
    dt_entrada = models.DateField(auto_now_add= True)
    dt_saida = models.DateField(null= True, blank= True)
    situacao = models.IntegerField(default= 1)

    def __str__(self):
        return self.usuario.nome
