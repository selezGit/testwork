import os

env = os.getenv('ENVIRONMENT', 'dev')

if env == 'dev':
    from .base import *  # noqa
elif env == 'test':
    from .test import *  # noqa
