from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutor.views import tutor_chat
from autostudy.views import TutorChatView
from study import admin


router = DefaultRouter()
  # Registra o viewset do chatbot


urlpatterns = [
     path('chat-tutor/', tutor_chat, name='tutor-chat'),
     path('api/tutor/chat/', tutor_chat, name='tutor-chat-api'),
    path('admin/', admin),  # Rota para o admin do Django
    path('api/users/', include('users.urls')),  # Inclui as rotas do app users
    path('chat/', TutorChatView.as_view(), name='tutor-chat'),  # Rota para o chatbot
    path('api-auth/', include('rest_framework.urls')),  # Para autenticação básica
]