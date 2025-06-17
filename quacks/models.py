from django.db import models
from django.conf import settings


class Quack(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quacks')
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} @ {self.created_at:%d-%m-%Y %H:%M}: "{self.body[:30]}..."'