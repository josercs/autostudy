from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_onboarding_completed = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    curso = models.CharField(max_length=100, blank=True, null=True)
    metas = models.TextField(blank=True, null=True)
    desempenho = models.JSONField(default=dict)
    nome = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    onboarding_completo = models.BooleanField(default=False)
    xp = models.IntegerField(default=0)
    nivel = models.IntegerField(default=1)

    
    
    estilo_aprendizado = models.CharField(max_length=50, blank=True, null=True)
    horas_estudo = models.IntegerField(default=5)
    trilha = models.CharField(max_length=50, blank=True, null=True)
    # Campos para o plano de estudos
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    goal = models.CharField(max_length=255, blank=True)

class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_study_plans')
    daily_study_time = models.IntegerField()
    study_tasks = models.TextField(blank=True)  # Adicionei o campo study_tasks

