from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autostudy.settings')

app = Celery('autostudy')

# Lê as configurações do Celery no arquivo settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente as tarefas em apps instalados
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
