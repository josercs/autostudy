from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Mensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens')
    mensagem = models.TextField()
    resposta = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario.username} em {self.data_criacao}"

class StudyPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tutor_studyplans'  # Nome exclusivo para evitar conflitos
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plano de Estudo de {self.user.username}"
