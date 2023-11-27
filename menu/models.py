from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='media/')
    SABOR_CHOICES = [
        ('Morango', 'Chocolate'),
        ('Limão', 'Ninho'),
        ('Doce de leite', 'Goiaba'),
        # Adicione mais opções conforme necessário
    ]
    sabor = models.CharField(max_length=20, choices=SABOR_CHOICES)
    
    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidade = models.BooleanField(default=True)

def __str__(self):
        return self.nome