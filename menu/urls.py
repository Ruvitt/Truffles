from django.urls import path
from django.contrib.auth.models import User
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('dashboard_cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('comprar_produto/', views.comprar_produto, name='comprar_produto')
]