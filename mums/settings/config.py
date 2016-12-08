import json
from settings.common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

with open('/etc/mums/settings.json') as file_config:
    config = json.loads(file_config.read())
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config['SECRET_KEY']

    # pylint: disable=undefined-variable
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASSWORD']
    }

    TIME_ZONE = config['TIME_ZONE']

    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_ROOT = config['STATIC_ROOT']
    ENVIRONMENT = config['ENVIRONMENT']

    if ENVIRONMENT == 'production':
        ALLOWED_HOSTS = ['*']
        DEBUG = False
        X_FRAME_OPTIONS = 'DENY'
        SECURE_CONTENT_TYPE_NOSNIFF = True
        SECURE_BROWSER_XSS_FILTER = True
    else:
        ALLOWED_HOSTS = []
        DEBUG = True
