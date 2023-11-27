from django.urls import path
from django.contrib.auth.models import User
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('login_vendedor/', views.login_vendedor, name='login_vendedor'),
    path('cadastro_vendedor/', views.cadastro_vendedor, name='cadastro_vendedor')
]