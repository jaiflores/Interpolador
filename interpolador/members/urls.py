'''Arquivo para listar as urls, funções e paginas em html da seção de login'''
from django.urls import path
from . import views

'''A pasta de html chamada "Templates", tem que ter uma outra pasta dentro, que no geral é com o mesmo nome do app, mas o app de login/logout/registro_user tem que ter a pasta com o nome "authenticate".'''
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]