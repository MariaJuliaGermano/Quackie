from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
import logging
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = User()
    novo_usuario.nome = request.POST.get('nome') # Aqui define o campo nome no models usuario, pegando de "nome"
    novo_usuario.email = request.POST.get('email') # Aqui define o campo email no models usuario, pegando de "email"
    novo_usuario.senha = request.POST.get('senha') # Aqui define o campo senha no models usuario, pegando de "senha"
    novo_usuario.save() 
    usuarios = {
        'usuarios': User.objects.all() # Colocando em um dicionário todos os objetos do models Usuario que foram cadastrados
    }
    return render(request, 'usuarios/usuarios.html', usuarios) # Aqui ele retorna a mudança de página para a página que vai listar os usuários cadastrados e em seguida a própria lista de usuários 

def search(request):
    return render(request, 'base/search.html')

def profile(request):
    return render(request, 'profile/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        return render(request, 'profile/profile_edit.html')

def post_create(request):
    return render(request, 'post/create.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {'error': 'Credenciais inválidas'})
    print("Requisição GET para a página de login.")
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Nome de usuário ou email já existe'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.save()
        return redirect('login')
    return render(request, 'auth/register.html')

def base(request):
    return render(request, 'base/landing.html')

def logout(request):
    return render(request, 'base/search.html')