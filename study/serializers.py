from rest_framework import serializers
from .models import Subject, Content, Question, Simulation
from django.contrib.auth import get_user_model
from rest_framework import serializers

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
from .models import StudyProgress

class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = '__all__'
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
