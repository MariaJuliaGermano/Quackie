from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('profile/', views.profile,name='profile'),
    path('profile-edit/', views.profile_edit,name='profile_edit'),
    path('logout', views.logout,name='logout')
]
