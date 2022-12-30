from datetime import datetime, timedelta

from apps.agendamento.models import *


def verificar_colaborador(preco, data, hora):
    colaboradores = []
    servico = preco.servico
    for item in ColaboradorServico.objects.filter(servico= servico):
        colaborador = item.colaborador
        if not Agendamento.objects.filter(servico= preco, data= data, hora= hora, colaborador= colaborador):
            colaboradores.append(colaborador)

    return colaboradores


def verificar_colaboradores(preco, date, valor):
    if Agendamento.objects.filter(servico= preco, data= date, hora= valor).exists():
        colaborares = ColaboradorServico.objects.filter(servico= preco.servico).count()
        if Agendamento.objects.filter(servico= preco, data= date, hora= valor).count() < colaborares:
            return False
    
    return True


def verificar_disponibildade(servico, horario, date, valor, intervalo_inicio, intervalo_fim, hora_inicio, hora_fim, hora_atual= None):
    preco = PrecoServico.objects.get(servico= servico, situacao= 1)
    if hora_atual:
        if hora_atual <= horario and verificar_colaboradores(preco, date, valor):
            return True
    else:
        if intervalo_inicio >= horario and verificar_colaboradores(preco, date, valor) and hora_inicio <= horario and horario <= hora_fim:
            return True
        elif horario >= intervalo_fim and verificar_colaboradores(preco, date, valor) and hora_inicio <= horario and horario <= hora_fim:
            return True
        
        return False


def consultar_servico(servico, date, hora_atual=None, minuto_atual=None, hora= None):
    if hora_atual:
        hora_atual = timedelta(hours= hora_atual, minutes= minuto_atual)

    duracao = servico.duracao
    hora_inicio = timedelta(hours=9)
    hora_fim = timedelta(hours=18)
    intervalo_inicio = timedelta(hours=12, minutes= 30)
    intervalo_fim = timedelta(hours=14)
    interalo = False

    horario = hora_inicio
    if hora:
        now = datetime.now()
        for i in range(1, 9, 1):
            if (now + timedelta(days=i)).date() == date:
                horario = hora.split(':')
                horario = timedelta(hours= int(horario[0]), minutes= int(horario[1]))
                return verificar_disponibildade(servico, horario, date, hora, intervalo_inicio, intervalo_fim, hora_inicio, hora_fim)
        
        return False

    horarios = []
    while horario < hora_fim:
        valor = str(horario).split(':')
        valor = f'{valor[0]}:{valor[1]}'

        if verificar_disponibildade(servico, horario, date, valor, intervalo_inicio, intervalo_fim, hora_inicio, hora_fim, hora_atual):
            horarios.append(valor)
        horario = horario + timedelta(minutes= duracao)
        
        if horario > intervalo_inicio and not interalo:
            interalo = True
            horario = intervalo_fim
    
    return horarios


def consultar_horarios(servico, hora= None):
    nome_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
    grades = []
    now = datetime.now()
    dias = 9
    
    hora_atual = int(now.strftime('%H'))
    minuto_atual = int(now.strftime('%M'))
    if hora_atual > 18 and len(consultar_servico(servico, now, hora_atual, minuto_atual)) > 0:
        grades.append({'data':now.date(),
            'nome': nome_semana[now.weekday()],
            'horarios': consultar_servico(servico, now, hora_atual, minuto_atual)})
        dias -= 1

    for i in range(0, dias, 1):
        date = now + timedelta(days=i)
        print(date)
        if date.weekday() != 6:
            grades.append({'data':date.date(),
                'nome': nome_semana[date.weekday()],
                'horarios': consultar_servico(servico, date)})
    
    return grades