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
        # Cria o usuário com a senha criptografada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Adiciona dados adicionais do usuário à resposta
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['curso'] = self.user.curso  # Se existir esse campo no modelo
        data['metas'] = self.user.metas if hasattr(self.user, 'metas') else []
        data['desempenho'] = self.user.desempenho if hasattr(self.user, 'desempenho') else {}

        return data