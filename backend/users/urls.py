from django.urls import path
from .views import (
    dados_usuario,
    chat_tutor,
    register,
    CustomTokenObtainPairView,
    completar_onboarding,
    OnboardingView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,  # Adicione isto se necessário
)
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('register/', register, name='auth-register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usuario/<int:usuario_id>/', dados_usuario),
    path('chat-tutor/', chat_tutor),
    path('onboarding/', completar_onboarding, name='completar_onboarding'),
    path('onboarding/view/', OnboardingView.as_view(), name='onboarding-view'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # E isto se necessário
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # E isto se necessário

]
