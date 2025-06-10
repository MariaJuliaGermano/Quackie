from django.contrib import admin
from django.urls import path
from AppSocialMedia import views

urlpatterns = [
    path('',views.base,name='base'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('profile/',views.profile,name='profile'),
    path('profile-edit/',views.profile_edit,name='profile_edit'),
    path('post/',views.post_create,name='post_create'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('admin/', admin.site.urls),
    path('logout',views.logout,name='logout')

]
