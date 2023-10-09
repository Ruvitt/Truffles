from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Cliente
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/admin') #enquanto não temos a home do cliente
        else:
            messages.error(request, 'Erro no telefone ou senha')
    return render(request, 'login_cliente.html')

def cadastro_cliente(request):
    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        user = User.objects.filter(username=username).first() # Verifica se o usuário já existe         
        # Cria o usuário e registra com adm
        if user is None:
            user = User.objects.create_user(username=username,  telefone=telefone)
            user.set_password(senha)
            user.is_active = True
            user.save()
            user
            cliente = Cliente(usuario=user, nome=nome)
            cliente.save()
            return redirect("login:login_adm")
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastro_cliente.html')
    
    return render(request, 'cadastro_cliente.html')