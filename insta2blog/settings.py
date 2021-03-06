"""
Django settings for insta2blog project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
PRODUCTION = False

ALLOWED_HOSTS = [
'https://insta2blog.herokuapp.com',
'http://insta2blog.herokuapp.com',
'insta2blog.herokuapp.com',
'https://www.insta2blog.com',
'http://www.minsta2blog.com',
'https://insta2blog.com',
'http://insta2blog.com',
'www.insta2blog.com',
'insta2blog.com',
'http://127.0.0.1:8000/',
'127.0.0.1',
'localhost:8000/',
'localhost'
]


# Application definition

INSTALLED_APPS = [
    'newsletter',
    'accounts',
    'core',
    'blog',

    # STUPID facebook API wont work with HTTP, they need HTTPS. This app below will help with that.
    # run the command below instead of python manage.py runserver
    # ./manage.py runserver_plus --cert /tmp/cert

    "sslserver",


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'insta2blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'insta2blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Local files
# STATIC_URL = '/static/'

# # # Copy data from here to server
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     #'/var/www/static/',
# ]
# # Server emmumator. One up DIR
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

# MEDIA_URL = "/media_cdn/"
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

###################################################################################

CUSTOM_PROJECT_NAME = "insta2blog"

AWS_STORAGE_BUCKET_NAME = 'side-projects'
AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET')



# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# NOW REPLACING THESE LINES TO USE OUR S3 BUCKET MORE ELEGANTLY.
# NOW WE WILL HAVE /static/ FOLDER FOR STATIC FILES, /media/ FOR OUR MEDIA FILES

# # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# # refers directly to STATIC_URL. So it's safest to always set it.
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
#
# # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# # you run `collectstatic`).
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# Grab all the files from here, and put them in the S3 Bucket!!
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Added this on 19th August. After learning from experiments on Ritrew app.


# I JUST ADDED A FILE NAMED cumstom_storages.py IN THE SAME DIRECTORY AS manage.oy
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, CUSTOM_PROJECT_NAME, STATICFILES_LOCATION)

# FROM HERE IS THE SETTINGS FOR MEDIA FILES
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, CUSTOM_PROJECT_NAME, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# THESE LINES WILL SAY THE EXPIRATION OF THIS DATA HAS NOT YET COME, SO USE THESE TILL IT EXPIRES.
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

