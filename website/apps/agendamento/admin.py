from django.contrib import admin

from apps.agendamento.models import *

# Register your models here.

class AgendamentoAdmin(admin.ModelAdmin):

    list_display = ('cliente', 'colaborador', 'servico', 'data', 'situacao', 'assinatura')
    list_filter = ('cliente', 'colaborador', 'servico', 'data', 'situacao', 'assinatura')
    search_fields = ['cliente', 'colaborador', 'servico', 'data', 'situacao', 'assinatura']


class ServicoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'duracao')
    list_filter = ('nome', 'duracao')
    search_fields = ['nome', 'duracao']


class PrecoServicoAdmin(admin.ModelAdmin):

    list_display = ('servico', 'valor_total', 'comissao', 'situacao')
    list_filter = ('servico', 'valor_total', 'comissao', 'situacao')
    search_fields = ['servico', 'valor_total', 'comissao', 'situacao']


class ColaboradorServicoAdmin(admin.ModelAdmin):

    list_display = ('servico', 'colaborador')
    list_filter = ('servico', 'colaborador')
    search_fields = ['servico', 'colaborador']


admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(PrecoServico, PrecoServicoAdmin)
admin.site.register(ColaboradorServico, ColaboradorServicoAdmin)
