from core.settings.base import *

DEBUG = True
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(',')

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('MONGO_DB_NAME'),
        'CLIENT': {
            'host': env('MONGO_HOST'),
            'port': env('MONGO_PORT'),
            'username': env('MONGO_DB_USERNAME'),
            'password': env('MONGO_DB_PASSWORD'),
        }
    }
}