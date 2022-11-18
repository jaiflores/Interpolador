'''Arquivo usado para fazer o formulario de registro, não é necessario, mas ao ser feio, posso controlar o que irá aparecer na pagina de registro. Os campos já são pré determinados pois utulizo nesse projeto o model "django.contrib.auth.forms".'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MeuUser(UserCreationForm):
    '''Classe criada para gerar a estrutura de form para adicionar o estudo no db. "Model vem do arquivo models, "fields" são informações que iram aparecer na página, "wigetes" é para ter formatação com css".'''
    class Meta:
        '''Para linkar o campo "labels" no formulario utiliza-se o '"name=""' "'''
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nome de Usuario',
            'first_name': 'Nome',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form'}),
            'first_name': forms.TextInput(attrs={'class':'form'}),
            'email': forms.EmailInput(attrs={'class':'form'}),
            'password1': forms.PasswordInput(attrs={'class':'form'}),
            'password2': forms.PasswordInput(attrs={'class':'form'}),
        }