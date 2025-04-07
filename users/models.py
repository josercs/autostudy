from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)  # Adicione o campo is_student

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    goal = models.CharField(max_length=255, blank=True)

class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_study_plans')
    daily_study_time = models.IntegerField()
    study_tasks = models.TextField(blank=True)  # Adicionei o campo study_tasks

