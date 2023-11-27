from django.urls import path, include
from django.contrib.auth.models import User
from login import views


app_name = 'login'
urlpatterns = [
    path('', views.home, name='home'),
    path('login_cliente/', views.login_cliente, name='login_cliente'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente')
] 
