from django.contrib import admin
from django.urls import path
from AppSocialMedia import views

urlpatterns = [
    # rota, view resposável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
