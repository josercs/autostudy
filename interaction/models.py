from django.db import models
from django.contrib.auth import get_user_model
from content.models import Disciplina, Topico

User = get_user_model()

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagens')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='postagens')
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='postagens', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.postagem.titulo}"

class Resposta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respostas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respostas')
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta de {self.autor.username} em {self.comentario.postagem.titulo}"
