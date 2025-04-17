from rest_framework import serializers
from .models import OnboardingStatus

class OnboardingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingStatus
        fields = ['completed']
