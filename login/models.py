from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Vendedor(models.model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidade = models.BooleanField(default=True)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    