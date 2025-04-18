# Generated by Django 5.1.8 on 2025-04-07 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topicos', to='content.disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='materialpdf',
            name='topico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materiais_pdf', to='content.topico'),
        ),
        migrations.AddField(
            model_name='videoaula',
            name='topico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='videoaulas', to='content.topico'),
            preserve_default=False,
        ),
    ]
