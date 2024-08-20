from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from feedback.services.get_feedback import get_feedback_scores

class FeedbackScoreAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            results = get_feedback_scores()
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
