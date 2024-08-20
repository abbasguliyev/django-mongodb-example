from core.settings.base import MONGO_CLIENT

def get_feedback_scores():
    client = MONGO_CLIENT
    db = client['qmeter']
    feedback_collection = db['qmeter']

    pipeline = [
        {
            '$unwind': "$feedback_rate"
        },
        {
            '$group': {
                '_id': {
                  'branch': '$branch.name'
                },
                'services': {
                    '$push': {
                        'service_name': '$feedback_rate.service.name',
                        'rating': '$feedback_rate.rate_option'
                    }
                }
            }
        },
        {
            '$unwind': '$services'
        },
        {
            '$group': {
                '_id': {
                    'branch': '$_id',
                    'service': '$services.service_name'
                },
                'ratings': {
                    '$push': '$services.rating'
                }
            }
        },
        {
            '$project': {
                'branch': '$_id.branch',
                'service': '$_id.service',
                'total_ratings': {'$size': '$ratings'},
                'ones': {
                    '$size': {
                        '$filter': {
                            'input': '$ratings',
                            'as': 'rating',
                            'cond': {'$eq': ['$$rating', 1]}
                        }
                    }
                },
                'twos': {
                    '$size': {
                        '$filter': {
                            'input': '$ratings',
                            'as': 'rating',
                            'cond': {'$eq': ['$$rating', 2]}
                        }
                    }
                },
                'threes': {
                    '$size': {
                        '$filter': {
                            'input': '$ratings',
                            'as': 'rating',
                            'cond': {'$eq': ['$$rating', 3]}
                        }
                    }
                },
                'fours': {
                    '$size': {
                        '$filter': {
                            'input': '$ratings',
                            'as': 'rating',
                            'cond': {'$eq': ['$$rating', 4]}
                        }
                    }
                },
                'fives': {
                    '$size': {
                        '$filter': {
                            'input': '$ratings',
                            'as': 'rating',
                            'cond': {'$eq': ['$$rating', 5]}
                        }
                    }
                }
            }
        },
        {
            '$project': {
                'branch': 1,
                'service': 1,
                'score': {
                    '$divide': [
                        {
                            '$multiply': [
                                100,
                                {
                                    '$add': [
                                        {'$multiply': ['$ones', 10]},
                                        {'$multiply': ['$twos', 5]},
                                        {'$multiply': ['$threes', 0]},
                                        {'$multiply': ['$fours', -5]},
                                        {'$multiply': ['$fives', -10]}
                                    ]
                                }
                            ]
                        },
                        {'$multiply': ['$total_ratings', 10]}
                    ]
                }
            }
        },
        {
            '$group': {
                '_id': '$branch',
                'services': {
                    '$push': {
                        'service_name': '$service',
                        'score': '$score'
                    }
                }
            }
        },
    ]
    
    results = list(feedback_collection.aggregate(pipeline))
    return results
