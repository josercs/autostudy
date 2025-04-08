# users/views.py
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        data = request.data
        
        # Validação básica
        if not all(k in data for k in ['username', 'email', 'password']):
            return Response(
                {'error': 'Missing required fields'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
        
    except IntegrityError:
        return Response(
            {'error': 'Username or email already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )