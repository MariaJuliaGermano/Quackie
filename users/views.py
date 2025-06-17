from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import logging
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        return render(request, 'users/profile_edit.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Credenciais inválidas'})
    print("Requisição GET para a página de login.")
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'error': 'Nome de usuário ou email já existe'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.save()
        return redirect('login')
    return render(request, 'users/register.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')