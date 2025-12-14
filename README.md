# 🗺️ Arrudeia - Plataforma de Turismo Urbano

<div align="center">

![Arrudeia Logo](django/arrudeia/static/assets/logo-arrudeia.png)

**Uma plataforma web para reconectar turistas e moradores com os espaços da cidade através de roteiros personalizados criados por guias locais certificados.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Estrutura de Banco de Dados](#-estrutura-de-banco-de-dados)
- [Desenvolvimento](#-desenvolvimento)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O **Arrudeia** é uma plataforma web desenvolvida em Django que visa promover a reconexão de turistas e moradores com os espaços urbanos da cidade. O projeto incentiva a caminhabilidade, valoriza a cultura local e oferece experiências personalizadas por meio de roteiros criados por guias certificados.

### Objetivos

- Tornar o turismo urbano mais acessível, imersivo e autêntico
- Permitir que cada usuário explore a cidade de acordo com seus interesses, necessidades e ritmo
- Conectar guias locais a pessoas que desejam vivências culturais mais ricas e informativas
- Promover um turismo mais humano, inclusivo e consciente

---

## ✨ Funcionalidades

### 🔐 Autenticação e Usuários
- **Sistema de Login e Cadastro**: Autenticação segura com Django Auth
- **Gerenciamento de Usuários**: Modelo personalizado de usuário com validações
- **Sessões**: Controle de acesso com login obrigatório para áreas restritas

### 🗺️ Roteiros
- **Feed de Roteiros**: Visualização de roteiros disponíveis
- **Roteiros Personalizados**: Filtros por interesses, perfil e região
- **Criação de Roteiros**: Interface para guias criarem novos roteiros
- **Níveis de Dificuldade**: Informações sobre tempo estimado e complexidade

### 📅 Eventos
- **Listagem de Eventos**: Visualização de eventos culturais e turísticos
- **Criação de Eventos**: Sistema para cadastro de novos eventos
- **Calendário**: Organização temporal dos eventos

### 👥 Guias Locais
- **Perfis de Guias**: Informações sobre guias certificados
- **Certificação**: Sistema de validação de guias locais
- **Contato**: Facilidade para entrar em contato com guias

### ❓ FAQ
- **Perguntas Frequentes**: Seção de dúvidas comuns
- **Suporte**: Informações sobre o uso da plataforma

### 🎨 Interface
- **Tema Claro/Escuro**: Alternância entre modos de visualização
- **Design Responsivo**: Interface adaptável a diferentes dispositivos
- **Navegação Intuitiva**: Menu de navegação claro e acessível

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+**: Linguagem de programação principal
- **Django 6.0**: Framework web de alto nível
- **SQLite**: Banco de dados (desenvolvimento)
- **Django Auth**: Sistema de autenticação integrado

### Frontend
- **HTML5**: Estrutura das páginas
- **CSS3**: Estilização e design responsivo
- **JavaScript**: Interatividade e funcionalidades dinâmicas
- **Font Awesome**: Ícones
- **Google Fonts**: Tipografia (Montserrat, Spline Sans Mono)

### Ferramentas de Desenvolvimento
- **Git**: Controle de versão
- **Virtual Environment**: Isolamento de dependências Python

---

## 📁 Estrutura do Projeto

```
pi_arrudeia_project/
│
├── django/                          # Projeto Django principal
│   ├── arrudeia/                    # App principal
│   │   ├── __init__.py
│   │   ├── admin.py                 # Configuração do admin Django
│   │   ├── apps.py
│   │   ├── models.py                # Modelos de dados (Usuario)
│   │   ├── views.py                 # Views e lógica de negócio
│   │   ├── urls.py                  # URLs do app
│   │   ├── tests.py
│   │   │
│   │   ├── migrations/              # Migrações do banco de dados
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   │   └── 0002_auto_20251214_0025.py
│   │   │
│   │   ├── static/                  # Arquivos estáticos
│   │   │   ├── assets/              # Imagens, logos, vídeos
│   │   │   ├── css/                 # Estilos CSS
│   │   │   │   ├── home.css
│   │   │   │   ├── homeoff.css
│   │   │   │   ├── feed.css
│   │   │   │   ├── eventos.css
│   │   │   │   ├── guias.css
│   │   │   │   ├── faq.css
│   │   │   │   ├── login.css
│   │   │   │   ├── post-eventos.css
│   │   │   │   ├── post-roteiros.css
│   │   │   │   ├── theme.css
│   │   │   │   ├── reset.css
│   │   │   │   └── style.css
│   │   │   │
│   │   │   └── js/                  # Scripts JavaScript
│   │   │       ├── script_home.js
│   │   │       ├── script_feed.js
│   │   │       └── theme_toggle.js
│   │   │
│   │   └── templates/                # Templates HTML
│   │       └── arrudeia/
│   │           ├── index.html       # Página inicial (logado)
│   │           ├── homeoff.html      # Página inicial (não logado)
│   │           ├── login.html        # Login e cadastro
│   │           ├── feed.html         # Feed de roteiros
│   │           ├── eventos.html      # Lista de eventos
│   │           ├── post-eventos.html # Criar evento
│   │           ├── guias.html        # Perfis de guias
│   │           ├── faq.html          # FAQ
│   │           └── post-roteiros.html # Criar roteiro
│   │
│   ├── sistema/                      # Configurações do projeto
│   │   ├── __init__.py
│   │   ├── settings.py               # Configurações Django
│   │   ├── urls.py                   # URLs principais
│   │   ├── wsgi.py                   # WSGI config
│   │   └── asgi.py                   # ASGI config
│   │
│   ├── db.sqlite3                    # Banco de dados SQLite
│   ├── manage.py                     # Script de gerenciamento Django
│   │
│   └── venv/                         # Ambiente virtual Python
│
└── Arrudeia_Django_w_Database/       # Versão alternativa do projeto
    └── [estrutura similar]
```

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)
- **Navegador web moderno** (Chrome, Firefox, Edge, etc.)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Rogrinhu/pi_arrudeia.git
cd pi_arrudeia
```

### 2. Navegue até o diretório do projeto Django

```bash
cd django
```

### 3. Crie e ative um ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install django
```

Ou, se houver um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://127.0.0.1:8000/`

---

## ⚙️ Configuração

### Configurações do Django

As principais configurações estão em `django/sistema/settings.py`:

- **SECRET_KEY**: Chave secreta do Django (altere em produção!)
- **DEBUG**: Modo de debug (desative em produção)
- **ALLOWED_HOSTS**: Hosts permitidos
- **DATABASES**: Configuração do banco de dados
- **STATIC_URL**: URL para arquivos estáticos

### Banco de Dados

O projeto utiliza **SQLite** por padrão. Para usar outro banco de dados (PostgreSQL, MySQL), edite `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arrudeia_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 💻 Uso

### Acessando a Plataforma

1. **Página Inicial (Não Logado)**: `http://127.0.0.1:8000/`
   - Visualização pública do site
   - Acesso a informações gerais

2. **Login**: `http://127.0.0.1:8000/login/`
   - Faça login com suas credenciais
   - Ou crie uma nova conta

3. **Páginas Principais**:
   - **Feed de Roteiros**: `/feed/`
   - **Eventos**: `/eventos/`
   - **Guias**: `/guias/`
   - **FAQ**: `/faq/`

### Painel Administrativo

Acesse o painel admin em: `http://127.0.0.1:8000/admin/`

Use as credenciais do superusuário criado anteriormente.

---

## 🗄️ Estrutura de Banco de Dados

### Modelo Usuario

```python
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
```

**Nota de Segurança**: A senha está sendo armazenada em texto plano no modelo `Usuario`. Em produção, utilize apenas o sistema de autenticação do Django (`User`), que faz hash das senhas automaticamente.

---

## 🔧 Desenvolvimento

### Criando Migrações

Após alterar os modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Coletando Arquivos Estáticos

```bash
python manage.py collectstatic
```

### Executando Testes

```bash
python manage.py test
```

### Modo Debug

O modo debug está ativado por padrão. Para produção, altere em `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### Padrões de Código

- Siga as convenções do PEP 8 para Python
- Use nomes descritivos para variáveis e funções
- Adicione comentários quando necessário
- Mantenha o código limpo e organizado

---

## 📝 Melhorias Futuras

- [ ] Implementar hash de senhas no modelo Usuario
- [ ] Adicionar sistema de avaliações e comentários
- [ ] Integração com APIs de mapas (Google Maps, Mapbox)
- [ ] Sistema de busca avançada de roteiros
- [ ] Upload de imagens para roteiros e eventos
- [ ] Sistema de notificações
- [ ] Suporte multilíngue completo
- [ ] API REST para integração com apps mobile
- [ ] Sistema de pagamento para reservas
- [ ] Dashboard para guias

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais informações.

---

## 👥 Autores

- **Equipe Arrudeia** - Desenvolvimento inicial

---

## 🙏 Agradecimentos

- Governo de Pernambuco
- Prefeitura de Recife
- SENAC
- Gerando Falcões
- Serasa Experian
- Recinplay

---

## 📞 Contato

Para dúvidas, sugestões ou problemas:

- **GitHub Issues**: [Abrir uma issue](https://github.com/Rogrinhu/pi_arrudeia/issues)
- **Email**: [seu-email@exemplo.com]

---

<div align="center">

**Desenvolvido com ❤️ para promover o turismo urbano e a cultura local**

</div>

