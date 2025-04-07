from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import UserCreateView


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
    path('api/study/', include('study.urls')),
    path('api/content/', include('content.urls')),
    path('api/interaction/', include('interaction.urls')),
    path('register/', UserCreateView.as_view(), name='user-register'),  # Adiciona a rota diretamente
    path('', home, name='home'),  # Rota para a URL raiz
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
