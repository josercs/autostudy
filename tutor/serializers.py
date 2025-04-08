from rest_framework import serializers
from .models import StudyPlan  # Certifique-se de que o modelo está sendo importado corretamente

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'