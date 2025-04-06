from rest_framework import viewsets, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Subject, Content, Question, Simulation
from .serializers import SubjectSerializer, ContentSerializer, QuestionSerializer, SimulationSerializer
from rest_framework import generics, permissions
from .models import Subject, Content
from .models import Question, Simulation
from .serializers import SubjectSerializer, ContentSerializer, QuestionSerializer, SimulationSerializer
from .models import StudyProgress
from .serializers import StudyProgressSerializer
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudyProgress
from .serializers import StudyProgressSerializer



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

# ✅ Lista pública de matérias
class PublicSubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

# ✅ Lista pública de conteúdos por matéria
class PublicContentBySubjectView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Content.objects.filter(subject_id=subject_id)



class StudyProgressViewSet(viewsets.ModelViewSet):
    serializer_class = StudyProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

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