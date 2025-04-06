from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Subject, Content, Question, Simulation

User = get_user_model()

class StudyModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.subject = Subject.objects.create(name='Matemática', description='Descrição de Matemática')
        self.content = Content.objects.create(subject=self.subject, title='Equações do 1º grau', content_type='video', url='https://example.com/video')
        self.question = Question.objects.create(
            content=self.content,
            question_text='Qual o valor de x em x + 2 = 5?',
            option_a='2',
            option_b='3',
            option_c='4',
            option_d='5',
            correct_option='B'
        )
        self.simulation = Simulation.objects.create(user=self.user, title='Simulado ENEM')
        self.simulation.questions.add(self.question)

    def test_subject_creation(self):
        self.assertEqual(str(self.subject), 'Matemática')  # Verifica se o __str__ retorna o nome

    def test_content_creation(self):
        self.assertEqual(self.content.title, 'Equações do 1º grau')

    def test_question_correct_option(self):
        self.assertEqual(self.question.correct_option, 'B')

    def test_simulation_questions(self):
        self.assertEqual(self.simulation.questions.count(), 1)
        self.assertEqual(self.simulation.questions.first(), self.question)
    def test_user_simulation(self):
        self.assertEqual(self.simulation.user.username, 'testuser')