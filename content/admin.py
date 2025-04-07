from django.contrib import admin
from .models import VideoAula, Quiz

@admin.register(VideoAula)
class VideoAulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
