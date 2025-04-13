from django.shortcuts import render
from rest_framework import viewsets
from .models import Postagem, Comentario, Resposta
from .serializers import PostagemSerializer, ComentarioSerializer, RespostaSerializer
from django_ratelimit.decorators import ratelimit
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.select_related('autor', 'disciplina', 'topico').prefetch_related('comentarios')
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.select_related('postagem', 'autor').prefetch_related('respostas')
    serializer_class = ComentarioSerializer

class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.select_related('comentario', 'autor')
    serializer_class = RespostaSerializer

@ratelimit(key='ip', rate='5/m', block=True)  # Limita a 5 requisições por minuto por IP
@api_view(['GET'])
def postagem_list(request):
    postagens = Postagem.objects.all()
    serializer = PostagemSerializer(postagens, many=True)
    return Response(serializer.data)
