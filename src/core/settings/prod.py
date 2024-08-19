from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(',')

CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(',')
CSRF_WHITELIST_ORIGINS =env("CSRF_TRUSTED_ORIGINS").split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}