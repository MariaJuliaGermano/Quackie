from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de refência
    path('',views.home,name="home"),
    path('usuarios/',views.usuarios,name='usuarios_cadastrados')

]
