from django import forms
from django.forms import ModelForm
from .models import Estudo

# form para adicionar estudo de usuário
class EstudoForm(ModelForm):
    '''Classe criada para gerar a estrutura de form para adicionar o estudo no db. "Model vem do arquivo models, "fields" são informações que iram aparecer na página, "wigetes" é para ter formatação com css"'''
    class Meta:
        model = Estudo
        fields = ('name_study','descricao', 'xy',) 
        labels = {
            'name_study': 'Nome do Estudo',
            'descricao': 'Descrição do Estudo',
            'xy': 'Valor de x e y',
            }
        widgets = {
            'name_study': forms.TextInput(attrs={'class':'form', 'placeholder':'Nome do Estudo'}),
            'descricao': forms.TextInput(attrs={'class':'form', 'placeholder':'Descrição do Estudo'}),
            'xy': forms.TextInput(attrs={'class':'form', 'placeholder':'Valor de x'}),
        }