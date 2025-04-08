from django.contrib import admin
from .models import User, UserProfile  # Remova StudyPlan se ele não pertence ao app users
from study.models import StudyPlan  # Certifique-se de importar o modelo correto

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'goal')

class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'created_at']  # Remova 'daily_study_time' se não existir

admin.site.register(StudyPlan, StudyPlanAdmin)
