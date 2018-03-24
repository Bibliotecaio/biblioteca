"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'api', 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l-5y((3c4$rkntuab!30-y*aj%^ey*4zzv%w&cw8)jgp_y443l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'web', 'api.rpsc-biblio.ru']

ADMIN_SITE_HEADER = 'Управление архивом'
ADMIN_SITE_TITLE = 'Управление архивом'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
    'redactor',

    'core',
    'documents',
    'publications',
    'users',
    'search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'apiapi/static/dist/bin'),
            os.path.join(BASE_DIR, 'api/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'api', 'static'),
)


AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = "noreply@site.com"


REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS':
        'core.paginators.CustomPagination',
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.TokenSerializer',
}

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'is_superuser': True
}

CORS_ORIGIN_ALLOW_ALL = True


STORAGE_INFO_URL = 'http://localhost:9000/storage-info/'
ADD_DOCUMENT_URL = 'http://localhost:9000/add-document/'
DOCUMENT_RANDOM_COUNT = 5

REDACTOR_OPTIONS = {'lang': 'ru', 'plugins': ['fontcolor']}
REDACTOR_UPLOAD = 'uploads/'
REDACTOR_FILE_STORAGE = 'core.storages.SeaweedfsStorage'

SEAWEEDFS_HOST = 'localhost'
SEAWEEDFS_PORT = 9333


SEAWEEDFS_VOLUME_HOST = 'http://localhost'
SEAWEEDFS_VOLUME_PORT = 8080

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'biblioteca',
        'USER': 'biblioteca',
        'PASSWORD': '123456',
        'HOST': 'db',
        'PORT': '5432',
    }
}

