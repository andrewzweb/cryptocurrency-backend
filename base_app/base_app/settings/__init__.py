''' settings '''

from .celery import app as celery_app

try:
    from .local import *
    print('[+] Run local settings ')
    __all__ = ('celery_app',)
except:
    from .production import *
    print('[+] Run production settings')
