from django.contrib import admin
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem', 'resposta', 'data_criacao')
    search_fields = ('usuario__username', 'mensagem', 'resposta')
