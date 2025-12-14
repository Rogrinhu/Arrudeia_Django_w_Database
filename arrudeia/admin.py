from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 10
    readonly_fields = ('id_usuario',)
    list_filter = ('nome', 'email')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('id_usuario', 'nome', 'email', 'senha')
        }),
    )

