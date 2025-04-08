from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyPlanViewSet

router = DefaultRouter()
router.register(r'study-plan', StudyPlanViewSet, basename='study-plan')

urlpatterns = [
    path('', include(router.urls)),
]