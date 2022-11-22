from django.contrib import admin

from apps.clube.models import *

# Register your models here.

class ClubeAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'mes', 'ano', 'situacao')
    search_fields = ['usuario', 'mes', 'ano', 'situacao']

admin.site.register(Clube, ClubeAdmin)