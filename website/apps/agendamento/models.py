from django.db import models

from apps.usuario.models import Colaborador, User

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.CharField(max_length=500)
    imagem = models.FileField(upload_to='static/media', max_length=100, blank= True, null= True)

    def __str__(self):
        return self.nome


    def path_url(self):
        return self.imagem.replace('static/', '')


class PrecoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
    dt_inicio = models.DateField(auto_now_add=True)
    dt_fim = models.DateField(null= True, blank= True)
    valor_total = models.FloatField()
    comissao = models.FloatField()
    situacao = models.IntegerField(default= 1)

    def __str__(self):
        return self.servico.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    servico = models.ForeignKey(PrecoServico, on_delete=models.DO_NOTHING)
    data = models.DateField()
    hora = models.CharField(max_length= 5)
    situacao = models.CharField(max_length= 20)
    assinatura = models.IntegerField(default=0)


class ColaboradorServico(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
