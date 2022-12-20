from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Adm(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dt_entrada = models.DateField(auto_now_add=True)
    dt_saida = models.DateField(null= True, blank= True)
    situacao = models.IntegerField(default= 1)

    def __str__(self):
        return self.usuario.username


class Colaborador(models.Model):
    usuario = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    dt_entrada = models.DateField(auto_now_add= True)
    dt_saida = models.DateField(null= True, blank= True)
    situacao = models.IntegerField(default= 1)

    def __str__(self):
        return self.usuario.username
