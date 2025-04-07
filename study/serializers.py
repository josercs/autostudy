from rest_framework import serializers
from .models import Subject, Content, Question, Simulation
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import StudyTask
from .models import StudyPlan
from .models import Notification
from .models import StudyProgress
from .models import StudentProfile


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = '__all__'

class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class StudyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTask
        fields = '__all__'

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'

    def validate_end_date(self, value):
        """
        Verifica se a data de término é posterior à data de início.
        """
        if value <= self.initial_data['start_date']:
            raise serializers.ValidationError("A data de término deve ser posterior à data de início.")
        return value

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
