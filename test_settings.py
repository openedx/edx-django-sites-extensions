"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'insecure-secret-key'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django_sites_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE = (
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django_sites_extensions.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'django_sites_extensions.tests.urls'

############## Settings for RedirectMiddleware ###############

# Setting this to None causes Redirect data to never expire
# The cache is cleared when Redirect models are saved/deleted
REDIRECT_CACHE_TIMEOUT = None  # The length of time we cache Redirect model data
REDIRECT_CACHE_KEY_PREFIX = 'redirects'
SITE_ID = 1
