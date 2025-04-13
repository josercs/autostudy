from celery import shared_task
from .models import Notification, User
from django.utils.timezone import now

@shared_task
def send_daily_study_reminders():
    users = User.objects.all()
    for user in users:
        Notification.objects.create(
            user=user,
            message="📚 Hora do estudo! Não se esqueça de revisar seus conteúdos hoje.",
        )
