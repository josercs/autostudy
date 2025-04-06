# study/serializers.py
from rest_framework import serializers
from .models import StudentProfile, StudyPlan, StudyTask

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class StudyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTask
        fields = '__all__'

class StudyPlanSerializer(serializers.ModelSerializer):
    tasks = StudyTaskSerializer(many=True, read_only=True)

    class Meta:
        model = StudyPlan
        fields = '__all__'
        extra_kwargs = {
            'student': {'required': False},  # Allow student to be optional for creation
        }
    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks', [])
        study_plan = StudyPlan.objects.create(**validated_data)
        for task_data in tasks_data:
            StudyTask.objects.create(plan=study_plan, **task_data)
        return study_plan