'''Arquivo para criar as funções que eram ser o motor para o funcionamento da página.'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EstudoForm
from .models import Estudo

def inicial(request):
    '''Função para quando o usuairio estiver na pagina inicial e não estiver logado'''
    return render(request, 'home/home.html')

def home(request):
    '''
    Função para aparecer a pagina inicial do site, sem estar logado
    '''
    return render(request, 'home/home.html')

def add_estudo(request):
    '''
    Função para adicionar estudo no banco de dados. Inicia-se com o submmit falso, para que só entre no no db a informaçao quando o usuario clique no botão de enviar.
    '''
    submitted = False
    if request.method == "POST":
        form = EstudoForm(request.POST)
        if form.is_valid():
            estudo = form.save(commit=False)
            estudo.owner = request.user.id
            estudo.save()
            return redirect('/estudo_list?submitted=True')
    else:
        form = EstudoForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/add_estudo.html', {'form': form ,'submitted': submitted})

def estudo_list(request):
    '''
    Função para redirecionar o login ou para acessar via menu na area logada do site. Ele referencia o models de Estudo.
    '''
    estudo_list = Estudo.objects.all()
    return render(request, 'home/estudo_list.html', 
    {'estudo_list': estudo_list})

def show_estudo(request, name_study_id):
    '''
    Função para mostrar o estudo que ja esta na base de dados, sendo assim para conferencia simples
    '''
    estudo_list = Estudo.objects.filter(pk=name_study_id)
    return render(request, 'home/show_estudo.html',{'estudo_list': estudo_list})

def search_estudo(request):
    '''
    Função para buscar algum estudo do usuario e mostrar na tela para simples conferencia ou atualizar ou deletar. Ele utiliza o nome do do estudo.
    '''
    if request.method == "POST":
        searched = request.POST['searched']
        estudos = Estudo.objects.filter(name_study__contains= searched)

        return render(request, 
        'home/search_estudo.html',
        {'searched':searched,
         'estudos': estudos})
    else:
            return render(request, 'home/search_estudo.html',{})
    
def update_estudo(request, estudo_id):
    '''
    Função para fazer atualizar os dados do estudo que já esta na base de dados.
    '''
    estudo = Estudo.objects.get(pk=estudo_id)
    form = EstudoForm(request.POST or None, instance=estudo)
    if form.is_valid():
        form.save()
        return redirect('/estudo_list')
    
    return render(request,'home/update_estudo.html', {'estudo': estudo, 'form':form})

def delete_estudo(request,estudo_id):
    '''
    Função para deletar o estudo no banco de dados.
    '''
    estudo_list = Estudo.objects.get(pk=estudo_id)
    estudo_list.delete()
    return redirect('/estudo_list')

def estudo_text(request, estudo_id):

    response = HttpResponse(content_type='text/plain')
    lines = []

    # Escolhendo o modelo
    estudos = Estudo.objects.filter(pk=estudo_id)
    nome = estudos[0].name_study
    descr = estudos[0].descricao
    xey = estudos[0].xy

    # trabalhando os dados recebidos
    xey_linhas = xey.split('\n')
    xey_lista = []
    for j in xey_linhas:
        xey_lista.append(j.split(';'))
    texto_base = ''
    for k in xey_lista:
        xey_texto = ' | '.join(k)
        texto_base += f'''{xey_texto}\n    '''

    lines.append(
        f'''Nome do estudo: {nome}
Descrição:
    {descr}
Valores observados:
    {texto_base}'''
    )

    response[
        'Content-Disposition'
    ] = f'attachment; filename={estudos[0].name_study}.txt'
    # Escrever no TextFile
    response.writelines(lines)
    return response