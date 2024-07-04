from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Usuario
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

def login_view(request):
    if request.method == "GET":
        return render(request, 'pagelogin.html')

    elif request.method == "POST":
        nome_usuario = request.POST.get('nomeUsuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=nome_usuario, password=senha)

        if user is not None:
            loginUser(request, user)
            return redirect('/Doacoes')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'pagelogin.html')

    return HttpResponse("Método HTTP não suportado.", status=405)

def cadastro(request):
    if request.method == "GET":
        return render(request, 'pagecadastro.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        nome_usuario = request.POST.get('nomeUsuario')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        tipo_usuario = request.POST.get('tipoUsuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')

        if senha == confirmar_senha:
            try:
                if tipo_usuario == '1' and not cpf:
                    messages.error(request, 'O campo CPF deve ser preenchido!')
                    return render(request, 'pagecadastro.html')

                if User.objects.filter(username=nome_usuario).exists():
                    messages.error(request, 'Este nome de usuário já está em uso')
                    return render(request, 'pagecadastro.html')

                if Usuario.objects.filter(cpf=cpf).exists():
                    messages.error(request, 'Este CPF já está em uso')
                    return render(request, 'pagecadastro.html')

                if Usuario.objects.filter(email=email).exists():
                    messages.error(request, 'Este email já está em uso')
                    return render(request, 'pagecadastro.html')

                user = User.objects.create_user(username=nome_usuario, password=senha)
                usuario = Usuario(nome=nome, cpf=cpf, nome_usuario=nome_usuario, email=email,
                                  telefone=telefone, tipo_usuario=tipo_usuario, user=user)
                usuario.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('/accounts/login')

            except Exception as err:
                messages.error(request, f'Erro interno: {err}')
                return render(request, 'pagecadastro.html')
        else:
            messages.error(request, 'As senhas não correspondem!')
            return render(request, 'pagecadastro.html')

    return HttpResponse("Método HTTP não suportado.", status=405)
