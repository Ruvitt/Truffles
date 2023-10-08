from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Cliente
from django.contrib import messages
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