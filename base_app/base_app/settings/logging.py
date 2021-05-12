LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        'rich': {
            'datefmt': '[%X]'
        },
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
      },
    'handlers': {
        'console': {
         'class': 'rich.logging.RichHandler',
         'formatter': 'rich'
     },
     'file': {
         'level': 'DEBUG',
         'class': 'logging.FileHandler',
         'formatter': 'file',
         'filename': 'debug.log'
     }
 },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}
