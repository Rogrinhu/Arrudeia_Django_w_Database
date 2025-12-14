from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (homeoff)
    path('', views.homeoff, name='homeoff'),
    
    # Página index (alternativa)
    path('index/', views.index, name='index'),
    
    # Login e cadastro
    path('login/', views.login_view, name='login'),
    
    # Logout
    path('logout/', views.logout_view, name='logout'),
    
    # Cadastro
    path('cadastro/', views.cadastro_view, name='cadastro_view'),
    
    # Feed de roteiros
    path('feed/', views.feed, name='feed'),
    
    # Eventos
    path('eventos/', views.eventos, name='eventos'),
    path('post-eventos/', views.post_eventos, name='post_eventos'),
    
    # Guias
    path('guias/', views.guias, name='guias'),
    
    # FAQ
    path('faq/', views.faq, name='faq'),
    
    # Post de roteiros
    path('post-roteiros/', views.post_roteiros, name='post_roteiros'),
]