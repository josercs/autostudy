from django.contrib import admin
from .models import Postagem, Comentario, Resposta

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'disciplina', 'data_criacao')
    list_filter = ('disciplina', 'topico', 'autor')
    search_fields = ('titulo', 'autor__username', 'disciplina__nome')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'autor', 'data_criacao')
    search_fields = ('postagem__titulo', 'autor__username')

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'autor', 'data_criacao')
    search_fields = ('comentario__postagem__titulo', 'autor__username')
