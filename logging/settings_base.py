import os
import logging

SENTRY_DSN = os.getenv('SENTRY_DSN')
SENTRY_ENVIRONMENT = os.getenv('SENTRY_ENVIRONMENT')

LOGGING = dict(
    version = 1,
    disable_existing_loggers = False,
    formatters = {
        'simple': {'format': '%(asctime)s %(levelname)-8s %(message)s'},
        'verbose': {
            'format': '%(asctime)s %(name)-12s %(module)s %(levelname)-8s %(message)s'  # noqa
        },
        'json': {
            'format': '%(created)s %(asctime)s %(levelname)s %(message)s %(module)s %(lineno)d',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    handlers = {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'level': logging.INFO,
            'stream': 'ext://sys.stdout'
        },
        'sentry': {
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
            'environment': SENTRY_ENVIRONMENT,
            'level': logging.ERROR
        }
    },
    loggers = {
        '': {
            'handlers': ['console', 'sentry'],
            'level': logging.INFO,
            'propagate': True
        },
        'gino.engine': {
            'propagate': False
        }
    }
)
