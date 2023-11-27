from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import models 
from .models import Vendedor
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

def cadastro_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        print(user, username, senha)
        if user is not None:
            login(request, user)
            return redirect('/menu')  # enquanto não temos a home do cliente logado
        else:
            messages.error(request, 'Erro no login ou senha')
    return render(request, 'login_cliente.html')
def cadastro_vendedor(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        disponibilidade = request.POST.get('disponibilidade')
        vendedor = Vendedor.objects.filter(user__username=username).first()  # Verifica se o usuário já existe


        # Cria o usuário e registra comum
        if vendedor is None:
            vendedor = Vendedor(nome=nome, telefone=telefone) 
            user = User.objects.create_superuser(username=username, password=senha)
            user.save()
            user
            vendedor.user = user
            vendedor.save()
             # Use o modelo CustomUser
            return redirect("menu:login_vendedor")
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastro_vendedor.html')

    return render(request, 'cadastro_vendedor.html')