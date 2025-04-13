from django.db import models
from django.conf import settings


class Mensagem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('processed', 'Processada'),
        ('error', 'Erro'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensagens')

    # 👈 Alterado para ForeignKey com related_name
    mensagem = models.TextField()
    resposta = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    origem = models.CharField(max_length=50, default='chat-tutor')  # 👈 NOVO CAMPO
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario.username} em {self.data_criacao}"
