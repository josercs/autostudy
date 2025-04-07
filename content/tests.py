from django.test import TestCase
from .models import VideoAula, Quiz, Pergunta, Opcao, MaterialPDF
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoAulaTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.videoaula = VideoAula.objects.create(
            titulo="Aula Teste",
            descricao="Descrição da aula",
            video="videos/teste.mp4",
            autor=self.user
        )

    def test_videoaula_creation(self):
        self.assertEqual(self.videoaula.titulo, "Aula Teste")
