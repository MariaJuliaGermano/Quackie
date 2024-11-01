from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, default="Your Name")
    email = models.EmailField(default="enteryour@email.com")
    senha = models.TextField(default="default_password")