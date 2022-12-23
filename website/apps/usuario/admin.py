from django.contrib import admin

from apps.usuario.models import *

# Register your models here.

class AdmAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_entrada', 'dt_saida', 'situacao')
    search_fields = ['usuario', 'dt_entrada', 'dt_saida', 'situacao']


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id_consumer', 'id_subscription', 'clube')
    search_fields = ['username', 'email', 'id_consumer', 'id_subscription', 'clube']


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Adm, AdmAdmin)
admin.site.register(User, UserAdmin)