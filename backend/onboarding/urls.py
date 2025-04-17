from django.urls import path
from .views import OnboardingStatusView

urlpatterns = [
    path('', OnboardingStatusView.as_view(), name='onboarding-status'),
]
