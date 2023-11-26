from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import models
from .models import Produto
from django.contrib import messages
from django.contrib.auth.models import User

def menu(request):
    produtos = Produto.objects.all()
    return render(request, 'dashboard_vendedor.html', {'produtos': produtos})

def registrar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST['nome_produto']
        preco_produto = request.POST['preco_produto']
        descricao_produto = request.POST['descricao_produto']
        imagem_produto = request.FILES['imagem_produto']
        produto = Produto.objects.create(nome_produto=nome_produto, preco_produto=preco_produto, descricao_produto=descricao_produto, imagem_produto=imagem_produto)
        produto.save()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('menu:menu')
    else:
        return render(request, 'registrar_produto.html')

def sair(request):
    logout(request)
    return redirect('login:home')