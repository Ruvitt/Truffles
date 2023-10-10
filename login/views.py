from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db import models
from .models import Cliente, CustomUserManager
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/home')  # enquanto não temos a home do cliente logado
        else:
            messages.error(request, 'Erro no telefone ou senha')
    return render(request, 'login_cliente.html')

def cadastro_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        user = CustomUserManager.objects.filter(username=username).first()  # Verifica se o usuário já existe

        # Cria o usuário e registra comum
        if user is None:
            user = CustomUserManager.objects.create_user(username=username, telefone=telefone)  # Use o modelo CustomUser
            user.set_password(senha)
            user.is_active = True
            user.save()

            cliente = Cliente(usuario=user, nome=nome)
            cliente.save()
            return redirect("login:login_adm")
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastro_cliente.html')

    return render(request, 'cadastro_cliente.html')
