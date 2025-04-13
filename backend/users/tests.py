from django.test import TestCase
from .models import User, UserProfile, StudyPlan

class UsersModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joao', password='123456', email='joao@example.com')
        self.profile = UserProfile.objects.create(user=self.user, birth_date='2000-01-01', goal='Passar no Enem')
        self.plan = StudyPlan.objects.create(user=self.user, daily_study_time=3)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'joao')
        self.assertTrue(self.user.check_password('123456'))

    def test_user_profile(self):
        self.assertEqual(self.profile.goal, 'Passar no Enem')

    def test_study_plan_time(self):
        self.assertEqual(self.plan.daily_study_time, 3)
