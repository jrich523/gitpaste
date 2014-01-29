import os

DEBUG = True

ALLOW_ANONYMOUS_POSTS = True
ALLOW_ANONYMOUS_ACCESS = True

REPO_DIR = os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'repositories'])

import os

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.sep.join([os.path.dirname(__file__), 'whoosh', 'search-index']),
    },
}


USE_ICONS = False

def generate_icon(email):
    """Generates the icon when a user is created. It should
    return the URL of the gravatar/desired avatar hosting."""
    import hashlib
    import urllib
    size = 40
    default = '/static/img/default-icon.png'
    gravatar = "http://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(email.lower()).hexdigest(),
            urllib.urlencode({'d':default, 's':str(size)}))
    return gravatar

USE_TZ = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

AUTH_PROFILE_MODULE = "paste.Profile"

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

GITHUB_APP_ID = 'aab29ec0a3e8e6307adf'
GITHUB_API_SECRET = 'e49d44e64abc587d2a50889030a195451109f8c0'
GITHUB_EXTRA_DATA = [
    ('avatar_url', 'avatar'),
    ('login', 'login'),
]

ADMINS = (
        ('Joel Bennett', 'Jaykul@HuddledMasses.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.abspath(os.path.dirname(__file__)),'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

# URL prefix for static files.
# Make sure to use a trailing slash.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "D:/home/site/wwwroot/PoshCode/paste/static",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '14qix7@zh_00qlyqw+$s(=e)^$7o8xfj(vpj0fws)y@7c1l^bc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'PoshCode.paste.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'PoshCode.urls'
ROOTDIR = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.sep.join([ROOTDIR, 'templates']),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.markup',
    'PoshCode.paste',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'haystack',
    'social_auth',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'filters': {
      'require_debug_false': {
         '()': 'django.utils.log.RequireDebugFalse'
      }
   },
   'handlers': {
      'mail_admins': {
         'level': 'ERROR',
         'filters': ['require_debug_false'],
         'class': 'django.utils.log.AdminEmailHandler'
      }
   },
   'loggers': {
      'django.request': {
         'handlers': ['mail_admins'],
         'level': 'ERROR',
         'propagate': True,
      },
   }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'PoshCode.context_processors.use_tz',
    'PoshCode.context_processors.use_icon',
    'PoshCode.context_processors.site',
)