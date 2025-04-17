from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views personalizadas
from users.views import CustomTokenObtainPairView, register
from .views import salvar_onboarding
from study import views as study_views
from tutor.views import tutor_chat

schema_view = get_schema_view(
    openapi.Info(
        title="AutoStudy API",
        default_version='v1',
        description="Documentação da API do AutoStudy",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@autostudy.local"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    return HttpResponse("Bem-vindo ao AutoStudy!")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Autenticação
    path('api/auth/register/', register, name='auth-register'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='auth-login'),  
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Endpoints específicos
    path('api/study/progress/', study_views.study_progress, name='study-progress'),
    path('api/tutor/chat/', tutor_chat, name='tutor-chat'),

    # Onboarding (duas rotas compatíveis com frontend)
    path('api/onboarding', salvar_onboarding, name='api-onboarding'),
    path('user/onboarding/', salvar_onboarding, name='user-onboarding'),
     

    # Apps
    path('api/users/', include('users.urls')),
    path('api/study/', include('study.urls')),
    path('api/ai/', include('ai_assistant.urls')),
    path('api/content/', include('content.urls')),
    path('api/interaction/', include('interaction.urls')),
    path("user/onboarding/", include("onboarding.urls")),


    # Documentação Swagger / ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # Frontend React (última rota para fallback SPA)
    path('', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
