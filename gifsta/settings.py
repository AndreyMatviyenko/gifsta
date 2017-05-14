"""
Django settings for gifsta project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z!0!v%won$u7vb#z2ne#km4t91)m6k$197fa8chv%bwx@6@9iq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gifspool',
    'social_django',
    # 'social_auth,'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',   
]

ROOT_URLCONF = 'gifsta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]




WSGI_APPLICATION = 'gifsta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/home/denys/projects/gifsta",
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2'    

    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.contrib.vk.VKOAuth2Backend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_KEY = '170616766788089'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '904a30830aea492f722a7e47598a5bdb'  # App Secret


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1030387813276-guf0v3h4k45tl06bet5d3o9hnrjvpsmu.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET= '7PSeS9R2Bpb6iu91FOWQVNyM'


SOCIAL_AUTH_VK_OAUTH2_KEY = 'aP2W5cG2inSiORz6lOWS'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '3ca99efb3ca99efb3ca99efb0c3cf59d5133ca93ca99efb65be850afdabf5957d922525'
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CELERY STUFF
CELERYD_OPTS="--autoscale=2,1 --concurrency=2 --processes=2 --pool=2"
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_IMPORTS = (
    "gifspool.tasks",
    "gifsta.celery",
    )


# CELERYBEAT_SCHEDULE = {
#     'every-minute': {
#         'task': 'for_run',
#         'schedule': timedelta(seconds=30), #crontab(minute='*/1'),
#         'args': [None],
#     }
# }