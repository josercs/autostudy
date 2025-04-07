from rest_framework.routers import DefaultRouter
from .views import (
    SubjectViewSet, ContentViewSet, QuestionViewSet, 
    SimulationViewSet, StudyProgressViewSet, StudyHistoryView,
    PublicSubjectListView, PublicContentBySubjectView, NotificationViewSet,
    ProgressoEstudoViewSet
)
from django.urls import path

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'simulations', SimulationViewSet)
router.register(r'progress', StudyProgressViewSet, basename='study-progress')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'progresso', ProgressoEstudoViewSet)

urlpatterns = [
    path('public/subjects/', PublicSubjectListView.as_view(), name='public-subjects'),
    path('public/subjects/<int:subject_id>/contents/', PublicContentBySubjectView.as_view(), name='public-contents-by-subject'),
    path('progress/history/', StudyHistoryView.as_view(), name='study-history'),
]

urlpatterns += router.urls