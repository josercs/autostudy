# study/tests/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from usuario.models import User
from study.models import StudyPlan

class StudyPlanTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.study_plan_url = reverse('studyplan-list')
        self.client.force_authenticate(user=self.user)

    def test_create_study_plan(self):
        data = {
            'title': 'Plan 1',
            'start_date': '2025-04-07',
            'end_date': '2025-06-07',
            'is_active': True
        }
        response = self.client.post(self.study_plan_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Plan 1')
        self.assertEqual(response.data['user'], self.user.id)