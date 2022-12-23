from datetime import datetime

from apps.agendamento.models import *


def servico_cadastro(request, servico= None):
    nome = request.POST.get('nome')
    duracao = request.POST.get('duracao')
    descricao = request.POST.get('descricao')
    
    servico = servico
    campos_invalidos = []

    if 10 > len(nome) < 150:
        campos_invalidos.append('Nome')

    if len(duracao) == 0:
        campos_invalidos.append('duracao')
    
    if servico == None:
        servico = Servico()
    
    servico.nome = nome
    servico.duracao = duracao
    servico.descricao = descricao
    servico.save()

    preco_cadastro(request, servico)

    return servico, campos_invalidos


def preco_cadastro(request, servico):
    valor = request.POST.get('valor')
    valor_comissao = request.POST.get('valor_comissao')

    if PrecoServico.objects.filter(servico= servico):
        preco = PrecoServico.objects.get(servico= servico)
        preco.dt_fim = datetime.today()
        preco.status = 0
        preco.save()

    preco = PrecoServico()
    preco.servico = servico
    preco.valor_total = valor
    preco.comissao = valor_comissao
    preco.save()

