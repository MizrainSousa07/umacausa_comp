from django.shortcuts import render, redirect
from .models import Doacao, Categoria, Usuario, Pedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/accounts/login') 

def umaCausa(request):
    if request.method == "GET": 
        user_authenticated = request.user.is_authenticated
        return render(request, 'indexd.html', {'user_authenticated': user_authenticated})

def doacoes(request):
    if request.method == "GET":
        doacoes = Doacao.objects.all()
        user_authenticated = request.user.is_authenticated
        return render(request, 'indexdoacoes.html', {'doacoes': doacoes, 'user_authenticated': user_authenticated})

def pedidos(request):
    if request.method == "GET":
        pedidos = Pedido.objects.all()
        user_authenticated = request.user.is_authenticated
        return render(request, 'indexpedidos.html', {'pedidos': pedidos, 'user_authenticated': user_authenticated})

@login_required(login_url='login')
def novaDoacao(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        id_categoria = request.POST.get('categoria')
        imagem = request.FILES.get('imagem')

        usuario_logado = request.user.id
        usu = Usuario.objects.get(id_usuario = usuario_logado)

        if descricao and id_categoria and imagem:
            categoria = Categoria.objects.get(pk=id_categoria)
            Doacao.objects.create(titulo = titulo, descricao=descricao, categoria=categoria, status='Aberta', imagem=imagem, usuario = usu)
            return redirect('/Doacoes')


    categorias = Categoria.objects.all()
    return render(request, 'novadoacaod.html', {'categorias': categorias})

@login_required(login_url='login')
def novoPedido(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        id_categoria = request.POST.get('categoria')

        usuario_logado = request.user.id
        usu = Usuario.objects.get(id_usuario = usuario_logado)

        if descricao and id_categoria and titulo:
            categoria = Categoria.objects.get(pk=id_categoria)
            Pedido.objects.create(titulo = titulo, descricao=descricao, categoria=categoria, status='Aberto', usuario = usu)
            return redirect('/Pedidos')


    categorias = Categoria.objects.all()
    return render(request, 'novopedido.html', {'categorias': categorias})

def verDoacao(request, id):
    if request.method == "GET":
        doacao = Doacao.objects.get( id_doacao = id )
        user_authenticated = request.user.is_authenticated
        return render(request, 'verdoacao.html', {'doacao' : doacao, 'user_authenticated': user_authenticated})

def verPedido(request, id):
    if request.method == "GET":
        pedido = Pedido.objects.get( id_pedido = id )
        user_authenticated = request.user.is_authenticated
        return render(request, 'verpedido.html', {'pedido' : pedido, 'user_authenticated': user_authenticated})

def concluirDoacao(request, id):
    concluir = Doacao.objects.get( id_doacao = id)
    concluir.status = 'Concluida'
    concluir.save()
    return redirect('/Doacoes')

def excluirDoacao(request, id):
    excluir = Doacao.objects.get( id_doacao = id)
    excluir.delete()
    return redirect('/Doacoes')

def concluirPedido(request, id):
    concluir = Pedido.objects.get( id_pedido = id)
    concluir.status = 'Concluido'
    concluir.save()
    return redirect('/Pedidos')

def excluirPedido(request, id):
    excluir = Pedido.objects.get( id_pedido = id)
    excluir.delete()
    return redirect('/Pedidos')

