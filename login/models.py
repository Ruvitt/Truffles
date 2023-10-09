from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=15, null=False, unique = True)
    telefone = models.CharField(max_length=11, null=False, unique=True)
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nome
