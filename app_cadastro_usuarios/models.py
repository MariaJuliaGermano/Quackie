from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(unique=True, default="enteryour@email.com")
    senha = models.TextField(default="default_password")