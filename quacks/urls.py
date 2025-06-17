from django.urls import path
from . import views


urlpatterns = [
    path('quack_create/', views.quack_create,name='quack_create')
]
