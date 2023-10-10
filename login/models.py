from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, login, senha, nome, telefone):
        if not login:
            raise ValueError("O campo de login deve ser preenchido")
        user = self.model(
            login=login,
            nome=nome,
            telefone=telefone,
        )
        user.set_password(senha)
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=15)
    telefone = models.CharField(max_length=11, unique=True)
    login = models.CharField(max_length=15, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'  # Defina aqui o campo a ser usado como nome de usuário

    def save(self, *args, **kwargs):
        # Faz a criptografia da senha antes de salvar o cliente
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.login


