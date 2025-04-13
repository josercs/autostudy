# users/urls.py
from django.urls import path
from .views import dados_usuario, chat_tutor, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('usuario/<int:usuario_id>/', dados_usuario),
    path('chat-tutor/', chat_tutor),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
