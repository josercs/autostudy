# study/urls.py
from rest_framework.routers import DefaultRouter
from .views import StudentProfileViewSet, StudyPlanViewSet, StudyTaskViewSet

router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet)
router.register(r'plans', StudyPlanViewSet)
router.register(r'tasks', StudyTaskViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path('profiles/', StudentProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-profile-list'),