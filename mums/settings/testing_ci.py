import os
from settings.common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# pylint: disable=undefined-variable
SECRET_KEY = '##DJANGO_SECRET##'

# pylint: disable=undefined-variable
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'dbIntranet.sqlite3')
}
