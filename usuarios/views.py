from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as loginUser
from django.contrib.auth.models import User

from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def login_view(request):
    if request.method == "GET":
        return render(request, 'pagelogin.html')
    
    elif request.method == "POST":
        nome_usuario = request.POST.get('nomeUsuario')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome_usuario).exists()

        user = authenticate(request, username=nome_usuario, password=senha)

        if not usuario:
            messages.info(request, 'Usuário não encontrado')
            return render(request, 'pagelogin.html')  # Retorne a página de login com uma mensagem de informação.
        elif user is not None:
            loginUser(request, user)
            return redirect('/Doacoes')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'pagelogin.html')  # Retorne a página de login com uma mensagem de erro.
    else:
        return HttpResponse("Método HTTP não suportado.", status=405)  # Retorna um erro de método não suportado para outras solicitações.
    
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

        def salvarCadastro():
            user = User.objects.create_user(username=nome_usuario, password=senha)
            usuario = Usuario(nome=nome, cpf=cpf, nome_usuario=nome_usuario, email=email, 
            telefone=telefone, tipo_usuario=tipo_usuario, user=user)
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('/accounts/login')

        if senha == confirmar_senha:
            try:
                if tipo_usuario == '1' and cpf == "":
                    messages.error(request, 'O campo CPF deve ser preenchido!')
                    return render(request, 'pagecadastro.html')

                elif User.objects.filter(username=nome_usuario).exists():
                    messages.error(request, 'Este nome de usuário já está em uso')
                    return render(request, 'pagecadastro.html')
                
                elif Usuario.objects.filter(cpf=cpf).exists():
                    messages.error(request, 'Este CPF já está em uso')
                    return render(request, 'pagecadastro.html')
                
                elif Usuario.objects.filter(email=email).exists():
                    messages.error(request, 'Este email já está em uso')
                    return render(request, 'pagecadastro.html')

                else:
                    salvarCadastro()
                    return render(request, 'pagecadastro.html')

            except Exception as err:
                messages.error(request, f'Erro interno: {err}')
                print(f'Erro interno: {err}')
                return render(request, 'pagecadastro.html')

        else:
            messages.error(request, 'As senhas não correspondem!')
            return render(request, 'pagecadastro.html')

    # Adicione um retorno padrão caso nenhum dos ramos acima seja atendido
    return HttpResponse("Método HTTP não suportado.", status=405)
        
