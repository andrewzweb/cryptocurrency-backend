''' production settings '''

from .base import *

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


# for django rest framework
DOMAIN_URL = 'http://some-domain-name.com'

# CORS for django-rest
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    DOMAIN_URL
)
