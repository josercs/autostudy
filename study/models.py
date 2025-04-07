from django.db import models
from users.models import User
from django.utils.timezone import now
from django.utils import timezone

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_study_plans')  # Alterado o related_name
    daily_study_time = models.IntegerField(default=0)  # Adicionado valor padrão

class StudyTask(models.Model):
    title = models.CharField(max_length=200, default="Tarefa sem título")  # Valor padrão válido
    due_date = models.DateField(default=now)  # Use timezone.now como valor padrão

class StudyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_progress')
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    progress_percent = models.FloatField(default=0.0)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'content')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']  # Notificações mais recentes primeiro

    def __str__(self):
        return f'Notification for {self.user.username}: {self.message}'