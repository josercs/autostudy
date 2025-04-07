from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Mensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens')
    mensagem = models.TextField()
    resposta = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario.username} em {self.data_criacao}"
