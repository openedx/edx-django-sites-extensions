import os

from os.path import join, abspath, dirname

# PATH vars
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('django_sites_extensions_SECRET_KEY', 'insecure-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.redirects',
    'django.contrib.sites',
)

PROJECT_APPS = (
    'django_sites_extensions',
)

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django_sites_extensions.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'django_sites_extensions.tests.urls'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Set this value in the environment-specific files (e.g. local.py, production.py, test.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Set up logging for development use (logging to stdout)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(process)d '
                      '[%(name)s] %(filename)s:%(lineno)d - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'requests': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING'
        },
        'factory': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING'
        },
        'django.request': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING'
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

############## Settings for RedirectMiddleware ###############

# Setting this to None causes Redirect data to never expire
# The cache is cleared when Redirect models are saved/deleted
REDIRECT_CACHE_TIMEOUT = None  # The length of time we cache Redirect model data
REDIRECT_CACHE_KEY_PREFIX = 'redirects'
