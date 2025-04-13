from rest_framework.routers import DefaultRouter
from .views import PostagemViewSet, ComentarioViewSet, RespostaViewSet

router = DefaultRouter()
router.register(r'postagens', PostagemViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'respostas', RespostaViewSet)

urlpatterns = router.urls