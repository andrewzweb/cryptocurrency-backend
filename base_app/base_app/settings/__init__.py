''' settings '''
import os

from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
      	return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_value('SECRET_KEY')

if get_env_value('DEVELOP'):
    from .local import *
    print('[+] Run local settings ')
else:
    from .production import *
    print('[+] Run production settings')
