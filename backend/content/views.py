from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Disciplina, Topico, VideoAula, MaterialPDF, Quiz, Pergunta, Opcao
from .serializers import (
    DisciplinaSerializer, TopicoSerializer, VideoAulaSerializer, MaterialPDFSerializer,
    QuizSerializer, PerguntaSerializer, OpcaoSerializer
)

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

class VideoAulaViewSet(viewsets.ModelViewSet):
    queryset = VideoAula.objects.all()
    serializer_class = VideoAulaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'topico__nome', 'topico__disciplina__nome']

class MaterialPDFViewSet(viewsets.ModelViewSet):
    queryset = MaterialPDF.objects.all()
    serializer_class = MaterialPDFSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'topico__nome', 'topico__disciplina__nome']

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class OpcaoViewSet(viewsets.ModelViewSet):
    queryset = Opcao.objects.all()
    serializer_class = OpcaoSerializer
