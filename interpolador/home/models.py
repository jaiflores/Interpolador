'''
Importações para que seja feito as inserções no banco de dados, inclusive fazerno a importação do "User" do modolo "django.contrib.auth.models", para ligar o user ao estudo.
'''
from django.db import models
from django.contrib.auth.models import User

class Estudo(models.Model):
    '''Informações que serão preenchidas na hora que o usuario for enviar os estudos para analizar. As funções abaixo serão para retorno no db'''
    name_study = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=240,blank=True)
    xy = models.TextField(max_length=240,blank=False)
    usuario_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    owner = models.IntegerField('User_id', blank=False)

    def __str__(self):
        return self.name_study
    def __repr__(self):
        return self.xy   
        