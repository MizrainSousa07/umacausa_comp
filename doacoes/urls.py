from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, DoacaoViewSet, PedidoViewSet, umaCausa, doacoes, pedidos, novaDoacao, novoPedido, verDoacao, verPedido, concluirDoacao, excluirDoacao, concluirPedido, excluirPedido

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'doacoes', DoacaoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('umaCausa/', umaCausa, name='umaCausa'),
    path('doacoes/', doacoes, name='doacoes'),
    path('pedidos/', pedidos, name='pedidos'),
    path('novaDoacao/', novaDoacao, name='novaDoacao'),
    path('novoPedido/', novoPedido, name='novoPedido'),
    path('verDoacao/<int:id>/', verDoacao, name='verDoacao'),
    path('verPedido/<int:id>/', verPedido, name='verPedido'),
    path('concluirDoacao/<int:id>/', concluirDoacao, name='concluirDoacao'),
    path('excluirDoacao/<int:id>/', excluirDoacao, name='excluirDoacao'),
    path('concluirPedido/<int:id>/', concluirPedido, name='concluirPedido'),
    path('excluirPedido/<int:id>/', excluirPedido, name='excluirPedido'),
]