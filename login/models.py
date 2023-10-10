from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=15)
    telefone = models.CharField(max_length=11, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
