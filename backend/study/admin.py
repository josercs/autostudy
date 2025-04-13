from django.contrib import admin
from .models import Subject, Content, Question, Simulation, ProgressoEstudo

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'content_type')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'content', 'correct_option')

@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    filter_horizontal = ('questions',)

@admin.register(ProgressoEstudo)
class ProgressoEstudoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'disciplina', 'topico', 'percentual_conclusao', 'ultima_atualizacao')
    list_filter = ('disciplina', 'topico', 'usuario')
    search_fields = ('usuario__username', 'disciplina__nome', 'topico__nome')
