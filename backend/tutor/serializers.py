from rest_framework import serializers
from .models import Mensagem  # Altere para o modelo correto, se necessário

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Mensagem
        fields = '__all__'