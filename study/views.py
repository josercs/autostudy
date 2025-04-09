from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from .models import (
    Subject, Content, Question, Simulation,
    StudyProgress, Notification, StudyPlan, StudyTask, StudentProfile, ProgressoEstudo
)
from .serializers import (
    SubjectSerializer, ContentSerializer, QuestionSerializer, SimulationSerializer,
    StudyProgressSerializer, NotificationSerializer, StudyPlanSerializer,
    StudyTaskSerializer, StudentProfileSerializer, ProgressoEstudoSerializer
)

from rest_framework.response import Response
from .models import StudyProgress
from .serializers import StudyProgressSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublicSubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]

class PublicContentBySubjectView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Content.objects.filter(subject_id=subject_id)

class StudyProgressViewSet(viewsets.ModelViewSet):
    serializer_class = StudyProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os progressos do usuário autenticado
        return StudyProgress.objects.filter(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudyHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        progress = StudyProgress.objects.filter(user=request.user).order_by('-last_accessed')
        serializer = StudyProgressSerializer(progress, many=True)
        return Response(serializer.data)

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os planos de estudo do usuário autenticado
        return self.queryset.filter(user=self.request.user)

class StudyTaskViewSet(viewsets.ModelViewSet):
    queryset = StudyTask.objects.all()
    serializer_class = StudyTaskSerializer
    permission_classes = [IsAuthenticated]

class ProgressoEstudoViewSet(viewsets.ModelViewSet):
    queryset = ProgressoEstudo.objects.all()
    serializer_class = ProgressoEstudoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__username', 'disciplina__nome', 'topico__nome']

@api_view(['GET'])
def study_progress(request):
    try:
        progress = StudyProgress.objects.filter(user=request.user)
        serializer = StudyProgressSerializer(progress, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

class StudyProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Exemplo de dados fictícios
        progress = [
            {"id": 1, "course_name": "Matemática", "progress_percentage": 75},
            {"id": 2, "course_name": "História", "progress_percentage": 50},
        ]
        return Response({"progress": progress})