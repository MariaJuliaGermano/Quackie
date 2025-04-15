from django.shortcuts import render
from AppSocialMedia.models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome') # Aqui define o campo nome no models usuario, pegando de "nome"
    novo_usuario.email = request.POST.get('email') # Aqui define o campo email no models usuario, pegando de "email"
    novo_usuario.senha = request.POST.get('senha') # Aqui define o campo senha no models usuario, pegando de "senha"
    novo_usuario.save() 
    usuarios = {
        'usuarios': Usuario.objects.all() # Colocando em um dicionário todos os objetos do models Usuario que foram cadastrados
    }
    return render(request, 'usuarios/usuarios.html', usuarios) # Aqui ele retorna a mudança de página para a página que vai listar os usuários cadastrados e em seguida a própria lista de usuários 