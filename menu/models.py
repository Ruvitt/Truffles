from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagem = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.nome