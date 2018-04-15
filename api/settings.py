from .base_settings import *

import os
import sys
PRJ_ROOT = os.path.normpath(os.path.dirname(__file__))

DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'biblioteca',
        'USER': 'biblioteca',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

