from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Produto
from django.contrib import messages

def menu(request):
    produtos = Produto.objects.all()
    return render(request, 'dashboard_vendedor.html', {'produtos': produtos})

def registrar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        preco_produto = request.POST.get('preco_produto')
        imagem_produto = request.FILES.get('imagem_produto')
        quantidade_produto = request.POST.get('quantidade_produto')
        sabor_produto = request.POST.get('sabor_produto')

        # Verificações
        if not nome_produto or not preco_produto or not imagem_produto or not quantidade_produto or not sabor_produto:
            messages.error(request, 'Preencha todos os campos.')
        elif not nome_produto.isalpha() or not sabor_produto.isalpha():
            messages.error(request, 'Os campos "Nome" e "Sabor" devem conter apenas letras.')
        elif float(preco_produto) < 0 or int(quantidade_produto) < 0:
            messages.error(request, 'Os campos "Preço" e "Quantidade" não podem ser negativos.')
        else:
            # Tudo está correto, podemos criar o produto
            Produto.objects.create(
                nome=nome_produto,
                preco=preco_produto,
                imagem=imagem_produto,
                quantidade=quantidade_produto,
                sabor=sabor_produto
            )
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('menu:menu')

    return render(request, 'registrar_produto.html')

def sair(request):
    logout(request)
    return redirect('login:home')
