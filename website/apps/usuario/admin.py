from django.contrib import admin

from apps.usuario.models import *

# Register your models here.

class AdmAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Adm, AdmAdmin)