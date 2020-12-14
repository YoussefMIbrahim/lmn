"""
Django settings for lmnop_project project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o+do-*x%zn!43h+unn!46(xp$e6&)=y63v#lj3ywjuy8cihz9f'

# if os.getenv('GAE_INSTANCE'):
#    # SECURITY WARNING: don't run with debug turned on in production!
#     DEBUG = False
# else:
#     DEBUG= True
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lmn',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lmnop_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'lmnop_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

    # Uncomment this when you are ready to use Postgres.

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lmnop-database',
        'USER' : 'lmnopuser',
        'PASSWORD' : os.getenv('LMNOPUSER_PW'),
        'HOST' : '/cloudsql/lmnop-122020:us-central1:lmnop-db1',
        'PORT' : '5432',
    },

    # And when you use Postgres, comment out or remove this DB config. 
    # Using environment variables to detect where this app is running, and automatically use 
    # an appropriate DB configuration, is a good idea.
    
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

if not os.getenv('GAE_INSTANCE'):
    DATABASES['default']['HOST'] = '127.0.0.1'
        
    


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#specify a location to copy static files to when running python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

#where in the file system to save user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if os.getenv('GAE_INSTANCE'):
    #read static files from the GS Bucket
    GS_STATIC_FILE_BUCKET = 'lmnop-122020.appspot.com'
    
    STATIC_URL = F'https://storage.cloud.google.com/{GS_STATIC_FILE_BUCKET}/static/'

    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

    GS_BUCKET_NAME = 'lmnop-user-images'
    
    MEDIA_URL = f'https://storage.cloud.google.com/{GS_BUCKET_NAME}/media/'

    from google.oauth2 import service_account
    GS_CREDENNTIALS = service_account.Credentials.from_service_account_file('lmnop-credentials.json')

else:
    #developing locally
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


# Where to send user after successful login, and logout, if no other page is provided.
LOGIN_REDIRECT_URL = 'my_user_profile'
LOGOUT_REDIRECT_URL = 'homepage'







