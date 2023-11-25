from django.urls import path
from django.contrib.auth.models import User
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('dashboard_vendedor/', views.dashboard_vendedor, name='dashboard_vendedor')
]