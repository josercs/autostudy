from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'curso', 'metas', 'desempenho']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email já registrado")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Renomeia os tokens para manter o padrão do frontend
        data['token'] = data.pop('access')
        data['refreshToken'] = data.pop('refresh')

        # Adiciona os dados do usuário no nível raiz do JSON
        data['user_id'] = user.id
        data['nome'] = user.nome
        data['email'] = user.email
        data['avatar'] = user.avatar.url if user.avatar else ''
        data['onboarding_completo'] = user.onboarding_completo
        data['xp'] = user.xp
        data['nivel'] = user.nivel

        return data


class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['estilo_aprendizado', 'horas_estudo', 'trilha', 'onboarding_completo']
