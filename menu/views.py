from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Produto
from login.models import Cliente, Vendedor
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def menu(request):
    produtos = Produto.objects.all()
    return render(request, 'dashboard_vendedor.html', {'produtos': produtos})


@login_required(login_url="login:login_cliente/")
def dashboard_cliente(request):
    produtos = Produto.objects.all()
    cliente = Cliente.objects.filter(id=request.user.id).first()
    context = {}
    context['produtos'] = produtos
    context['cliente'] = cliente
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

def comprar_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    if request.method == 'POST':
        quantidade_produto = request.POST.get('quantidade_produto')
    try:
        quantidade = int(quantidade_produto)
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        # Verifique se a quantidade está disponível em estoque
        if quantidade > produto.quantidade:
            raise ValueError("Quantidade indisponível em estoque.")
    
    except ValueError as e:
        # Trate o erro e forneça uma resposta adequada ao usuário
        return render(request, 'sua_template_de_erro.html', {'erro': str(e)})
        

def sair(request):
    logout(request)
    return redirect('login:home')
