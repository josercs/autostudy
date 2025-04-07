from django.urls import path
from .views import tutor_chat

urlpatterns = [
    path('chat/', tutor_chat, name='tutor-chat'),
]