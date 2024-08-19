from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.settings.base import env
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient

class FeedbackScoreAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # MongoDB ilə əlaqə
        client = MongoClient('mongodb://localhost:27017/')
        db = client['qmeter']
        feedback_collection = db['qmeter']

        # Məlumatları qruplaşdırmaq
        
        pipeline = [
            {'$unwind': '$feedback_rate'},
            {'$group': {
                '_id': {
                    'branch': '$branch.name',
                    'service': '$feedback_rate.service.name'
                },
                'rates': {'$push': '$feedback_rate.rate_option'}
            }},
            {'$project': {
                '_id': 0,
                'branch': '$_id.branch',
                'service': '$_id.service',
                'score': {
                    '$multiply': [
                        100,
                        {
                            '$divide': [
                                {
                                    '$add': [
                                        {'$multiply': ["$rateCounts.one", 10]},
                                        {'$multiply': ["$rateCounts.two", 5]},
                                        {'$multiply': ["$rateCounts.three", 0]},
                                        {'$multiply': ["$rateCounts.four", -5]},
                                        {'$multiply': ["$rateCounts.five", -10]}
                                    ]
                                },
                                "$rateCounts.total"
                            ]
                        },
                        10
                    ]
                }
            }}
        ]

        try:
            results = list(feedback_collection.aggregate(pipeline))
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Nəticələri qaytarmaq
        return Response(results, status=status.HTTP_200_OK)
