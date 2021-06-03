''' settings '''

try:
    from .local import *
    print('[+] Run local settings ')
except:
    from .production import *
    print('[+] Run production settings')
