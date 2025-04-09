from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import UserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from study import views as study_views
from users import views as user_views
from users.views import register  # Import the register function

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
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/study/', include('study.urls')),  # Inclui as rotas do app study
    path('api/ai/', include('ai_assistant.urls')),
    path('api/content/', include('content.urls')),
    path('api/interaction/', include('interaction.urls')),
    path('register/', user_views.register, name='register'),  # Endpoint para registro de usuários
    path('register/', register, name='register'),  # Endpoint para registro de usuários
    path('', TemplateView.as_view(template_name='index.html')),  # Rota para servir o React
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Endpoints para autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obter o token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para atualizar o token

    path('register/', user_views.register, name='register'),
    path('api/study/progress/', study_views.study_progress, name='study-progress'),

    # Documentação da API
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('study/', include('study.urls')),  # Inclui as rotas do app "study"
    path('api/', include('users.urls')),  # Inclui as rotas do app "users"
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

