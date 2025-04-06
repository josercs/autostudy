# ============================
# 3. models.py (study/models.py)
# ============================
from django.db import models
from users.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target_exam = models.CharField(max_length=50, choices=[
        ('ENEM', 'ENEM'),
        ('CONCURSO', 'Concurso Público'),
        ('VESTIBULAR', 'Vestibular'),
        ('REFORCO', 'Reforço Escolar'),
    ])
    available_hours_per_week = models.IntegerField(default=10)
    learning_style = models.CharField(max_length=50, choices=[
        ('video', 'Vídeo'),
        ('leitura', 'Leitura'),
        ('pratica', 'Prática'),
        ('misto', 'Misto'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

class StudyPlan(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class StudyTask(models.Model):
    plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name="tasks")
    subject = models.CharField(max_length=100)
    content_type = models.CharField(max_length=50, choices=[
        ('video', 'Vídeo'),
        ('leitura', 'Leitura'),
        ('exercicio', 'Exercício'),
        ('flashcard', 'Flashcard'),
    ])
    scheduled_date = models.DateField()
    completed = models.BooleanField(default=False)
