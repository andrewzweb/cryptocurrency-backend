''' local settings '''

from .base import *

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

# cors for djangorest
CORS_ORIGIN_ALLOW_ALL = True # allow any requests

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
