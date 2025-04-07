from rest_framework import serializers
from .models import Disciplina, Topico, VideoAula, MaterialPDF, Quiz, Pergunta, Opcao

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = '__all__'

class VideoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAula
        fields = '__all__'

class MaterialPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialPDF
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'

class OpcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcao
        fields = '__all__'