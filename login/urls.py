from django.urls import path, include
from django.contrib.auth.models import User
from login import views


app_name = 'login'
urlpatterns = [
    path('', views.home, name='home'),
]