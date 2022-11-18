from django.contrib import admin
from .models import Estudo

@admin.register(Estudo)
class EstudoAdmin(admin.ModelAdmin):
    '''
    Quando o html base de adicionar Estudo estiver completo, mudar esse campo, para aparecer.
    '''
    list_display = ('owner','name_study','descricao', 'xy',)
    ''' 
    Quando o fk estiver sendo gerado automaticamente, colocar o campo "study_id" como forma de listar por oredem.
    '''
    ordering = ('descricao',) 
    search_fields = ('descricao','xy','name_study',) 