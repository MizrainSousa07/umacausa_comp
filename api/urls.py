from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuario/<int:id>', views.usuario, name='usuario'),
    path('dadosUsuarios/', views.gerenciar_usuarios, name= 'gerenciar_usuarios'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido/<int:id>', views.pedido, name='pedido'),
    path('dadosPedidos/', views.gerenciar_pedidos, name= 'gerenciar_pedidos'),
]