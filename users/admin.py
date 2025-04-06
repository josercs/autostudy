# ============================
# 4. admin.py (users/admin.py e study/admin.py)
# ============================
from django.contrib import admin
from .models import User  # ou StudentProfile, StudyPlan, StudyTask

admin.site.register(User)