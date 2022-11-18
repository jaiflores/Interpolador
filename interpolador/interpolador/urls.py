'''Importações dos apps que estão sendo desenvolvidos para o projedo. O primeiro path, já vem adicionado na hora que criamos o projeto com o django, os demais são colocados manualmente.'''
from django.contrib import admin
from django.urls import path, include

'''Como o sistema de login do django tem um modolo que regula todo o processo, ele também precisa ser incluido nessa lista de urls'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

'''Personalização da área de administração do site'''
# Configure Admin Titles
admin.site.site_header = "Interpolador - Adminitration page"
admin.site.site_title = "Interpolador"
admin.site.index_title = "Interpolador"