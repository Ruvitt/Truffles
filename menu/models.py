from django.db import models
from django.contrib.auth.models import User

class Sabor(models.TextChoices):
    CHOCOLATE = 'chocolate', 'Chocolate'
    DOCE_DE_LEITE = 'doce_de_leite', 'Doce de leite'
    MORANGO = 'morango', 'Morango'

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    sabor = models.CharField(max_length=20, choices=Sabor.choices)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='media/')

    def get_produto(self):
        return Produto.objects.filter(produto_id=self.id)

    def __str__(self):
        return self.nome

    
