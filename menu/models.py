from django.db import models
from django.contrib.auth.models import User

class Sabor (models.TextChoices):
    chocolate = 'chocolate', 'Chocolate'
    doce_de_leite = 'doce_de_leite', 'Doce de leite'
    morango = 'morango', 'Morango'

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='media/')
    sabor = models.CharField(max_length=20, choices=Sabor.choices)
    
    def __str__(self):
        return self.nome