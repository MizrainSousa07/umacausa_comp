from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from usuarios.models import Usuario
from doacoes.models import Pedido
from .serializers import UsuarioSerializer, PedidoSerializer
import json

@api_view(['GET'])
def usuarios(request):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()

        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def usuario(request, id):

    try:
        usuario = Usuario.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciar_usuarios(request):

    if request.method == 'GET':
        
        try:
            if request.GET['id_usuario']:
                id_usuario = request.GET['id_usuario']

                try:
                    usuario = Usuario.objects.get(id_usuario= id_usuario)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



    if request.method == 'POST':

        novo_usuario = request.data

        serializer = UsuarioSerializer(data=novo_usuario)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PUT':

        id_usuario = request.data['id_usuario']

        try:
            atualizar_usuario = Usuario.objects.get(pk = id_usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioSerializer(atualizar_usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':

        id_usuario = request.data['id_usuario']

        try:
            deletar_usuario = Usuario.objects.get(pk= id_usuario)
            deletar_usuario.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pedidos(request):

    if request.method == 'GET':
        pedidos = Pedido.objects.all()

        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pedido(request, id):

    try:
        pedido = Pedido.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciar_pedidos(request):

    if request.method == 'GET':
        
        try:
            if request.GET['id_pedido']:
                id_pedido = request.GET['id_pedido']

                try:
                    pedido = Pedido.objects.get(pk= id_pedido)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = PedidoSerializer(pedido)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



    if request.method == 'POST':

        novo_pedido = request.data

        serializer = PedidoSerializer(data=novo_pedido)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PUT':

        id_pedido = request.data['id_pedido']

        try:
            atualizar_pedido = Pedido.objects.get(pk = id_pedido)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PedidoSerializer(atualizar_pedido, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':
        print(request.data)
        if 'id_pedido' in request.data:
            id_pedido = request.data['id_pedido']
            print(id_pedido)

            try:
                deletar_pedido = Pedido.objects.get(pk=id_pedido)
                print(deletar_pedido)
                deletar_pedido.delete()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            except Pedido.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'ID do pedido não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

# class DeletarPedidoViewSet(viewsets.ViewSet):
#     def destroy(self, request, id=None):
#         try:
#             deletar_pedido = Pedido.objects.get(pk=id)
#             deletar_pedido.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Pedido.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)