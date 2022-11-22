from django.contrib import admin

from apps.agendamento.models import *

# Register your models here.

class AgendamentoAdmin(admin.ModelAdmin):

    list_display = ('cliente', 'colaborador', 'servico', 'data', 'valor_total', 'situacao')
    list_filter = ('cliente', 'colaborador', 'servico', 'data', 'valor_total', 'situacao')
    search_fields = ['cliente', 'colaborador', 'servico', 'data', 'valor_total', 'situacao']

admin.site.register(Agendamento, AgendamentoAdmin)


class ServicoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'duracao', 'valor_total', 'comissao')
    list_filter = ('nome', 'duracao', 'valor_total', 'comissao')
    search_fields = ['nome', 'duracao', 'valor_total', 'comissao']

admin.site.register(Servico, ServicoAdmin)