from django.contrib import admin

from apps.usuario.models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email', 'senha')
    search_fields = ['nome', 'email', 'senha']

admin.site.register(Usuario, UsuarioAdmin)


class AdmAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']

admin.site.register(Adm, AdmAdmin)


class ColaboradorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']

admin.site.register(Colaborador, ColaboradorAdmin)