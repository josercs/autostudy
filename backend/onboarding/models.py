from django.db import models
from django.conf import settings

class OnboardingStatus(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Onboarding: {'Concluído' if self.completed else 'Pendente'}"
