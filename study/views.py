from rest_framework import viewsets, permissions, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    Subject, Content, Question, Simulation,
    StudyProgress, Notification, StudyPlan, StudyTask, StudentProfile, ProgressoEstudo
)
from .serializers import (
    SubjectSerializer, ContentSerializer, QuestionSerializer, SimulationSerializer,
    StudyProgressSerializer, NotificationSerializer, StudyPlanSerializer,
    StudyTaskSerializer, StudentProfileSerializer, ProgressoEstudoSerializer
)

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
        return StudyProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

class StudyTaskViewSet(viewsets.ModelViewSet):
    queryset = StudyTask.objects.all()
    serializer_class = StudyTaskSerializer
    permission_classes = [IsAuthenticated]

class ProgressoEstudoViewSet(viewsets.ModelViewSet):
    queryset = ProgressoEstudo.objects.all()
    serializer_class = ProgressoEstudoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__username', 'disciplina__nome', 'topico__nome']