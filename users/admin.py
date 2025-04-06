from django.contrib import admin
from .models import User, UserProfile  # Remova StudyPlan se ele não pertence ao app users
from study.models import StudyPlan  # Importe de study.models, se necessário

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'goal')

@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_study_time')
