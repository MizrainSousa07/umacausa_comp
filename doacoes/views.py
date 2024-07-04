from django.shortcuts import render, redirect
from .models import Doacao, Categoria, Pedido
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CategoriaSerializer, DoacaoSerializer, PedidoSerializer

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def umaCausa(request):
    if request.method == "GET":
        user_authenticated = request.user.is_authenticated
        return Response({'user_authenticated': user_authenticated})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doacoes(request):
    if request.method == "GET":
        doacoes = Doacao.objects.all()
        serializer = DoacaoSerializer(doacoes, many=True)
        return Response({'doacoes': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pedidos(request):
    if request.method == "GET":
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response({'pedidos': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def novaDoacao(request):
    if request.method == 'POST':
        titulo = request.data.get('titulo')
        descricao = request.data.get('descricao')
        id_categoria = request.data.get('categoria')
        imagem = request.FILES.get('imagem')

        usuario_logado = request.user.id
        usu = Usuario.objects.get(id_usuario=usuario_logado)

        if descricao and id_categoria and imagem:
            categoria = Categoria.objects.get(pk=id_categoria)
            doacao = Doacao.objects.create(titulo=titulo, descricao=descricao, categoria=categoria, status='Aberta', imagem=imagem, usuario=usu)
            serializer = DoacaoSerializer(doacao)
            return Response(serializer.data, status=201)

    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response({'categorias': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def novoPedido(request):
    if request.method == 'POST':
        titulo = request.data.get('titulo')
        descricao = request.data.get('descricao')
        id_categoria = request.data.get('categoria')

        usuario_logado = request.user.id
        usu = Usuario.objects.get(id_usuario=usuario_logado)

        if descricao and id_categoria and titulo:
            categoria = Categoria.objects.get(pk=id_categoria)
            pedido = Pedido.objects.create(titulo=titulo, descricao=descricao, categoria=categoria, status='Aberto', usuario=usu)
            serializer = PedidoSerializer(pedido)
            return Response(serializer.data, status=201)

    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response({'categorias': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verDoacao(request, id):
    if request.method == "GET":
        doacao = Doacao.objects.get(id_doacao=id)
        serializer = DoacaoSerializer(doacao)
        return Response({'doacao': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verPedido(request, id):
    if request.method == "GET":
        pedido = Pedido.objects.get(id_pedido=id)
        serializer = PedidoSerializer(pedido)
        return Response({'pedido': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def concluirDoacao(request, id):
    concluir = Doacao.objects.get(id_doacao=id)
    concluir.status = 'Concluida'
    concluir.save()
    serializer = DoacaoSerializer(concluir)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def excluirDoacao(request, id):
    excluir = Doacao.objects.get(id_doacao=id)
    excluir.delete()
    return Response(status=204)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def concluirPedido(request, id):
    concluir = Pedido.objects.get(id_pedido=id)
    concluir.status = 'Concluido'
    concluir.save()
    serializer = PedidoSerializer(concluir)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def excluirPedido(request, id):
    excluir = Pedido.objects.get(id_pedido=id)
    excluir.delete()
    return Response(status=204)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer
    permission_classes = [IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
