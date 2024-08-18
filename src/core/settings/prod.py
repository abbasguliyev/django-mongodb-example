from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(',')

CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(',')
CSRF_WHITELIST_ORIGINS =env("CSRF_TRUSTED_ORIGINS").split(',')

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('MONGO_DB_NAME'),
        'CLIENT': {
            'host': env('MONGO_HOST'),
            'port': int(env('MONGO_PORT', 27017)),
            'username': env('MONGO_DB_USERNAME'),
            'password': env('MONGO_DB_PASSWORD'),
        }
    }
}