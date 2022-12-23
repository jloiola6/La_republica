from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    id_consumer = models.CharField(max_length=150, blank= True, null= True)
    id_subscription = models.CharField(max_length=150, blank= True, null= True)
    clube = models.IntegerField(default=0)


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
        return self.usuario.first_name
