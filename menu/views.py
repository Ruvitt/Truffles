from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Produto
from login.models import Cliente, Vendedor
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def menu(request):
    produtos = Produto.objects.all()
    return render(request, 'dashboard_vendedor.html', {'produtos': produtos})


@login_required(login_url="login:/login_cliente/")
def dashboard_cliente(request):
    produtos = Produto.objects.all()
    context = {}
    context['produtos'] = produtos
    context['cliente'] = Cliente.objects.filter(user_id=request.user.id).first()
    return render(request, 'dashboard_cliente.html', context)

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

def comprar_produto(request, pk):
    produto = Produto.objects.filter(id=pk).first()
    if request.method == 'POST':
        quantidade_produto = request.POST.get('quantidade_produto')
        sabor_produto = request.POST.get('sabor_produto')
        
        # Verificações de validade da quantidade
        if quantidade_produto <= 0:
            return render(request, {'mensagem': 'A quantidade deve ser maior que zero.'})

        if quantidade_produto > produto.quantidade:
            return render(request, {'mensagem': 'A quantidade desejada excede o estoque disponível.'})
        
        try:
            quantidade_produto = int(quantidade_produto)
        except ValueError:
            return render(request, 'dashboard_cliente.html', {'mensagem': 'A quantidade deve ser um número inteiro válido.'})

        
        produto.quantidade -= quantidade_produto
        produto.save()


        return HttpResponseRedirect('/dashboard_cliente/')

    return render(request, 'dashboard_cliente.html', {'produto': produto}, {'sabor': sabor_produto})
    
def sair(request):
    logout(request)
    return redirect('login:home')
