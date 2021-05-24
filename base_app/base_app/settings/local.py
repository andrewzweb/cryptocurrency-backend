''' local settings '''

from .base import *
#from .logging import *

SECRET_KEY = 'django-insecure--hfhg76!do@za-ln3&pg9*(2x2sb^-k=he6)p2vrd&$ram$izo'
DEBUG = True
ALLOWED_HOSTS = ['*']

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev-db.sqlite3',
        # for correct test websocket app dashboard
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
}

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home/static'),
]

# cors for djangorest
CORS_ORIGIN_ALLOW_ALL = True # allow any requests

# Channels
ASGI_APPLICATION = "base_app.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': [
#        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#    ],
#}

# REST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

#AUTH_USER_MODEL = 'account.User'

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'account.utils.my_jwt_response_handler'
}
