from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Página Inicial
@login_required(login_url='login')
def index(request):
    """Página inicial (requer login)"""
    return render(request, 'arrudeia/index.html')

def homeoff(request):
    """Página inicial sem login"""
    return render(request, 'arrudeia/homeoff.html')

def feed(request):
    """Feed de roteiros"""
    return render(request, 'arrudeia/feed.html')

def eventos(request):
    """Página de eventos"""
    return render(request, 'arrudeia/eventos.html')

def guias(request):
    """Página de guias"""
    return render(request, 'arrudeia/guias.html')

def faq(request):
    """Página de perguntas frequentes"""
    return render(request, 'arrudeia/faq.html')

def post_eventos(request):
    """Página de post de evento"""
    return render(request, 'arrudeia/post-eventos.html')

def post_roteiros(request):
    """Página de post de roteiro"""
    return render(request, 'arrudeia/post-roteiros.html')

#Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        if not username or not password:
            messages.error(request, 'Preencha todos os campos')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'arrudeia/login.html')

#Logout
def logout_view(request):
    logout(request)
    return redirect('homeoff')

#Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        terms = request.POST.get('terms', '')
        
        # Debug: verificar se os dados estão chegando
        print(f"DEBUG - Dados recebidos: username={username}, email={email}, password={'*' * len(password)}, terms={terms}")
        print(f"DEBUG - Método: {request.method}, POST data: {dict(request.POST)}")
        
        if not username or not email or not password:
            messages.error(request, 'Preencha todos os campos')
        elif not terms:
            messages.error(request, 'Você deve aceitar os termos de privacidade')
        elif Usuario.objects.filter(nome=username).exists():
            messages.error(request, 'Usuário já existe')
        elif Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já existe')
        else:
            try:
                # Criar usuário na tabela usuarios (model Usuario)
                usuario = Usuario.objects.create(
                    nome=username,
                    email=email,
                    senha=password  # Nota: em produção, isso deve ser hash
                )
                print(f"DEBUG - Usuário criado na tabela usuarios: {usuario.nome} (ID: {usuario.id_usuario})")
                
                # Também criar no User do Django para autenticação funcionar
                # Isso mantém a compatibilidade com o sistema de autenticação do Django
                user = User.objects.create_user(username=username, email=email, password=password)
                print(f"DEBUG - Usuário criado no Django User para autenticação: {user.username} (ID: {user.id})")
                
                messages.success(request, 'Usuário criado com sucesso! Faça login para continuar.')
                return redirect('login')
            except Exception as e:
                print(f"DEBUG - Erro ao criar usuário: {str(e)}")
                import traceback
                traceback.print_exc()
                messages.error(request, f'Erro ao criar usuário: {str(e)}')
    return render(request, 'arrudeia/login.html')
