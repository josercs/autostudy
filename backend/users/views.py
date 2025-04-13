# users/views.py
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])  # Permite acesso público ao endpoint
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'user': user.username,
            'email': user.email,
            'message': 'Registro bem-sucedido'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def dados_usuario(request, usuario_id):
    try:
        usuario = User.objects.get(id=usuario_id)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado'}, status=404)

@api_view(['POST'])
def chat_tutor(request):
    usuario_id = request.data.get('usuario_id')
    pergunta = request.data.get('mensagem')

    try:
        usuario = User.objects.get(id=usuario_id)
        desempenho = usuario.desempenho

        # Lógica simples baseada em desempenho
        if 'matematica' in pergunta.lower():
            nota = desempenho.get('matematica', 0)
            if nota < 60:
                resposta = "Você está com desempenho baixo em matemática. Sugiro revisar frações e resolver mais exercícios."
            else:
                resposta = "Seu desempenho em matemática está bom! Continue praticando com questões de nível avançado."
        else:
            resposta = "Analisando seus dados. Em breve trarei sugestões personalizadas para você!"

        return Response({"resposta": resposta})
    
    except User.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado'}, status=404)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer