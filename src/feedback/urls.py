from django.urls import path
from .views import FeedbackScoreAPIView

urlpatterns = [
    path('feedback-stats/', FeedbackScoreAPIView.as_view(), name='feedback_stats'),
]