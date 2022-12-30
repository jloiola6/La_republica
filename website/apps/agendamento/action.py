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

    if PrecoServico.objects.filter(servico= servico, situacao= 1):
        preco = PrecoServico.objects.get(servico= servico, situacao= 1)
        preco.dt_fim = datetime.today()
        preco.situacao = 0
        preco.save()

    preco = PrecoServico()
    preco.servico = servico
    preco.valor_total = valor
    preco.comissao = valor_comissao
    preco.save()


def colaborador_servico_associar(request, servico):
    colaborador = request.POST.get('colaborador')

    if Colaborador.objects.filter(id= colaborador).exists() and servico:
        colaborador = Colaborador.objects.get(id= colaborador)

        if not ColaboradorServico.objects.filter(colaborador= colaborador, servico= servico).exists():
            colaborador_servico = ColaboradorServico()
            colaborador_servico.colaborador = colaborador
            colaborador_servico.servico = servico
            colaborador_servico.save()


def agendamento(request, usuario, preco, data, hora):
    colaborador = request.POST.get('colaborador')
    colaborador = Colaborador.objects.get(id= colaborador)

    if not Agendamento.objects.filter(colaborador= colaborador, cliente= usuario, servico= preco, data= data, hora= hora).exists():
        agendameto = Agendamento()
        agendameto.colaborador = colaborador
        agendameto.cliente = usuario
        agendameto.servico = preco
        agendameto.data = data
        agendameto.hora = hora
        agendameto.situacao = 'Reservado'
        agendameto.assinatura = usuario.clube
        agendameto.save()
                       