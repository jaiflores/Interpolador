'''Arquivo para criação de funções de login e registro do projeto. É importado do modol django.contrib as formas de como isso será feito'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MeuUser

def login_user(request):
	'''Função para login na pagina, só funciona se o usuario já tiver feito cadastro.'''
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		'''O "authenticate" é uma função do modolo do django.contrib.auth'''
		user = authenticate(request, username=username, password=password)
		'''Se o login for feito com sucesso, ele abre a pagina com a lista do estudos, se não logar retorna uma mensagem de erro e e retorna para a pagina de login'''
		if user is not None:
			login(request, user)
			return redirect('/estudo_list')
		else:
			messages.success(request, ("Username ou senha não conferem. Verifique e tente novamente!"))	
			return redirect('login')	
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, (" Você não esta logado! "))	
    return redirect('/home')

def register_user(request):
	'''Fução utilizada para registrar usuario no db, assim como a função "login_user". utiliza o model de django.contrib.auth'''
	if request.method == "POST":
		# form = RegisterUserForm(request.POST)
		form = MeuUser(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request,user)
			messages.success(request, ("Registro concluido!"))
			return redirect('/home')
	else:
		# form = RegisterUserForm()
		form = MeuUser()

	return render (request, 'authenticate/register_user.html', {'form': form})
	
