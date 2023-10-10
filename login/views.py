from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db import models
from .models import Cliente
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def login_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        print(user, username, senha)
        if user is not None:
            login(request, user)
            return redirect('/home')  # enquanto não temos a home do cliente logado
        else:
            messages.error(request, 'Erro no login ou senha')
    return render(request, 'login_cliente.html')

def cadastro_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cliente = Cliente.objects.filter(user__username=username).first()  # Verifica se o usuário já existe

        # Cria o usuário e registra comum
        if cliente is None:
            cliente = Cliente(nome=nome, telefone=telefone) 
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            user
            cliente.user = user
            cliente.save()
             # Use o modelo CustomUser
            return redirect("login:login_cliente")
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastro_cliente.html')

    return render(request, 'cadastro_cliente.html')
