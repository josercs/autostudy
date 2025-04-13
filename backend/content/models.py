from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

User = get_user_model()

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']  # Ordena por nome

class Topico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    disciplina = models.ForeignKey(Disciplina, related_name='topicos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']  # Ordena por nome

class VideoAula(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    video = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, related_name='videoaulas', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class MaterialPDF(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    arquivo_pdf = models.FileField(
        upload_to='pdfs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, related_name='materiais_pdf', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']  # Ordena por título

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='perguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name='opcoes', on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto
