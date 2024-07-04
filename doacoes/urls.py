from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('UmaCausa/', views.umaCausa, name='umacausa'),
    path('Doacoes/', views.doacoes, name='doacoes'),
    path('Pedidos/', views.pedidos, name='pedidos'),
    path('verDoacao/<int:id>', views.verDoacao, name='verdoacao'),
    path('verPedido/<int:id>', views.verPedido, name='verpedido'),
    path('concluirdoacao/<int:id>', views.concluirDoacao, name='concluirdoacao'),
    path('excluirdoacao/<int:id>', views.excluirDoacao, name='excluirdoacao'),
    path('concluirpedido/<int:id>', views.concluirPedido, name='concluirpedido'),
    path('excluirpedido/<int:id>', views.excluirPedido, name='excluirpedido'),
    path('novaDoacao/', views.novaDoacao, name='novadoacao'),
    path('novoPedido/', views.novoPedido, name='novopedido'),
    path('logout/', views.logout_view, name='logout')            
]