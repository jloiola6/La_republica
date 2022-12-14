from django.db import models
# from djstripe.models import Product


# from apps.usuario.models import Usuario

# # Create your models here.

# # class AssinaturaClube(models.Model):
# #     usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
# #     mes = models.CharField(max_length=20)
# #     ano = models.CharField(max_length=4)
# #     situacao = models.IntegerField(default= 1)


# class Clube(models.Model):
#     nome = models.CharField(max_length=100)
#     assinatura = models.ForeignKey(AssinaturaClube, on_delete=models.DO_NOTHING)


# class InscricaoClube(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
#     customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
#     subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)

    # class Meta:
    #     abstract = True

class LinkPagamento(models.Model):
    produto = models.CharField(max_length=50, blank= True, null= True)
    link = models.CharField(max_length=500, blank= True, null= True)
