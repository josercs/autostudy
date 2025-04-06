# no study/admin.py
from django.contrib import admin
from .models import StudentProfile, StudyPlan, StudyTask

admin.site.register(StudentProfile)
admin.site.register(StudyPlan)
admin.site.register(StudyTask)
