from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import OnboardingStatus
from .serializers import OnboardingStatusSerializer

class OnboardingStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        onboarding, _ = OnboardingStatus.objects.get_or_create(user=request.user)
        serializer = OnboardingStatusSerializer(onboarding)
        return Response(serializer.data)

    def post(self, request):
        onboarding, _ = OnboardingStatus.objects.get_or_create(user=request.user)
        onboarding.completed = True
        onboarding.save()
        return Response({'message': 'Onboarding concluído'}, status=status.HTTP_200_OK)
