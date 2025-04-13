from rest_framework.routers import DefaultRouter
from .views import (
    DisciplinaViewSet, TopicoViewSet, VideoAulaViewSet, MaterialPDFViewSet,
    QuizViewSet, PerguntaViewSet, OpcaoViewSet
)

router = DefaultRouter()
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'topicos', TopicoViewSet)
router.register(r'videoaulas', VideoAulaViewSet)  # Certifique-se de que está registrado apenas uma vez
router.register(r'materiais_pdf', MaterialPDFViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'perguntas', PerguntaViewSet)
router.register(r'opcoes', OpcaoViewSet)

urlpatterns = router.urls