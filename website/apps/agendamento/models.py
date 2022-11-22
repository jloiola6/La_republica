from django.db import models

from apps.usuario.models import Usuario, Colaborador

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.CharField(max_length=500)
    valor_total = models.FloatField()
    comissao = models.FloatField()

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
    data = models.DateField()
    hora = models.CharField(max_length= 10)
    situacao = models.CharField(max_length= 20)
    assitura = models.IntegerField(default=0)
    
    valor_total = models.FloatField()
    valor_comissao = models.FloatField()
    comissao = models.FloatField()