# autostudy/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao AutoStudy!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/study/', include('study.urls')),
    path('', home),  # Adiciona uma rota para a URL raiz
]
