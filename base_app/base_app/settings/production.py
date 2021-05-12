''' production settings '''

from .base import *

DOMAIN_URL = 'http://some-domain-name.com'

SECRET_KEY = 'django-insecure--hfhg76!do@za-ln3&pg9*(2x2sb^-k=he6)p2vrd&$ram$izo'
DEBUG = False
ALLOWED_HOSTS = ['*']

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# CORS for django-rest
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    DOMAIN_URL
)

# Channels
ASGI_APPLICATION = "base_app.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # TODO: change ip to docker like
            # "hosts": [('redis', 6379)],
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
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'account.utils.my_jwt_response_handler'
}
