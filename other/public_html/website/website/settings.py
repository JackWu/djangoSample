# Django settings for website project.
import os

ROOT_PATH = os.path.dirname(__file__)
#/home/devttagit/public_html/website/website
LOG_PATH = os.path.join('/', 'home', 'devttagit', 'public_html', 'log')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 'django',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

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
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g*n79wfefc(5m8k&amp;=v_&amp;xe4x!ka^!sp3y=9z=$0if^gg67zxo)'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'website.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
		os.path.join(ROOT_PATH, '../mypay/html'),
#		os.path.join(ROOT_PATH, '../paypal/standard/pdt'),
#		os.path.join(ROOT_PATH, '../paypal/standard/ipn'),
#		os.path.join(ROOT_PATH, '../mypal/templates_pro'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
		'mypay',
		'paypal.standard.ipn',
		'paypal.standard.pdt',
#		'paypal.pro',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
						'format':'[%(levelname)s] %(asctime)s [%(module)s] %(process)d [%(thread)d] %(message)s'
            #'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            #'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, "dev.ttagit.log"),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'dev.ttagit.logger': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
		'formatters':{
      'verbose':{
        'format':'%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
      },
      'simple':{
        'format':'%(levelname)s %(message)s'
      },
    },
    'handlers': {
        'file_dev_ttagit':{
          'level':'INFO',
          'class':'logging.FileHandler',
          'formatter':'verbose',
          'filename':os.path.join(LOG_PATH, 'dev.ttagit.log')
        },
    },
    'loggers': {
				'logview.dev_ttagit':{
					'handler':['file_dev_ttagit'],
					'level':'INFO',
					'propagate':True,
				},
    },
}"""
PAYPAL_RECEIVER_EMAIL = 'jack.w_1338396608_biz@ttagit.com'
PAYPAL_IDENTITY_TOKEN ='jF7kpfTnLgzVztKqoTiG0uNknYu1qD6k2tAp65qerkL0WM6I2RBnAlbtT5O'
PAYPAL_TEST = True
PAYPAL_WPP_USER = "jack.w_1343843708_biz_api1.ttagit.com"
PAYPAL_WPP_PASSWORD = "1343843853"
PAYPAL_WPP_SIGNATURE ="AuKxTnJwUrNP2CODDvXe1Lk7sjoVAlVmiS57TdgitiMOEg7rIkv4P4E8"
