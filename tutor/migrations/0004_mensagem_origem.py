# Generated by Django 5.1.8 on 2025-04-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_delete_studyplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='origem',
            field=models.CharField(default='chat-tutor', max_length=50),
        ),
    ]
