from django.db import models
from django.contrib.auth import get_user_model
from content.models import Disciplina, Topico, VideoAula, Quiz
from users.models import User
from django.utils.timezone import now
from django.utils import timezone
from django.conf import settings

User = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=100)  # Certifique-se de que o campo 'name' existe
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name  # Retorna o nome do assunto como string

class Content(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('article', 'Article'), ('pdf', 'PDF')])
    url = models.URLField()

class Question(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class Simulation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simulations')
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    goal = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class StudyPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='study_studyplans'  # Certifique-se de que o related_name é único
    )
    description = models.TextField(default="Plano de estudo padrão")  # Adicione um valor padrão
    created_at = models.DateTimeField(auto_now_add=True)  # Define a data/hora automaticamente

    def __str__(self):
        return f"Plano de Estudo de {self.user.username}"

class StudyTask(models.Model):
    title = models.CharField(max_length=200, default="Tarefa sem título")  # Valor padrão válido
    due_date = models.DateField(default=now)  # Use timezone.now como valor padrão

class StudyProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)  # Certifique-se de que este campo está definido
    progress_percentage = models.FloatField(default=0.0)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.course_name}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']  # Notificações mais recentes primeiro

    def __str__(self):
        return f'Notification for {self.user.username}: {self.message}'

class ProgressoEstudo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progresso_estudo')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='progresso_estudo')
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='progresso_estudo', null=True, blank=True)
    video_aula = models.ForeignKey(VideoAula, on_delete=models.CASCADE, related_name='progresso_estudo', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='progresso_estudo', null=True, blank=True)
    percentual_conclusao = models.FloatField(default=0.0)
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField(default=0)
    tempo_estudo = models.DurationField(default="00:00:00")  # Tempo total de estudo
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.disciplina.nome} - {self.percentual_conclusao}%"

    class Meta:
        unique_together = ('usuario', 'disciplina', 'topico', 'video_aula', 'quiz')
        ordering = ['-ultima_atualizacao']