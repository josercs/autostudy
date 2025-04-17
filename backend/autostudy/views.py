from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['POST'])
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


@api_view(["POST"])
def salvar_onboarding(request):
    estilo = request.data.get("estilo_aprendizado")
    usuario_id = request.data.get("usuario_id", "anon")
    # Aqui você pode salvar no banco ou logar
    print(f"Estilo: {estilo} | Usuário: {usuario_id}")
    return Response({"status": "sucesso"})


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Adiciona dados extras do usuário
        data['user_id'] = self.user.id
        data['nome'] = self.user.first_name or self.user.username
        data['avatar'] = getattr(self.user, 'avatar', '')
        data['nivel'] = getattr(self.user, 'nivel', 1)
        data['xp'] = getattr(self.user, 'xp', 0)
        data['onboarding_completo'] = getattr(self.user, 'onboarding_completo', False)

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer