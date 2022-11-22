from django.db import models

from apps.usuario.models import Usuario

# Create your models here.

class Clube(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    mes = models.CharField(max_length=20)
    ano = models.CharField(max_length=4)
    situacao = models.IntegerField(default= 1)