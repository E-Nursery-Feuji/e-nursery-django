"""
Django settings for e_nursery project.

Generated by 'django-admin startproject' using Django 4.1.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j%n3irt3!1c_4iibbhupnzhf#xt0l*!i^=yk2hptx9q$i_53td'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#AUTHNETICATION MODEL
AUTH_USER_MODEL = 'customer_app.Customer'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', #avoid cross origin error
    'rest_framework',  #provide python restful api services
    'admin_app.apps.AdminAppConfig',
    'customer_app.apps.CustomerAppConfig',
    'orders_app.apps.OrdersAppConfig',
    'products_app.apps.ProductsAppConfig',
   
    
]

CROSSHEADERS_ALLOWED_HEADERS = ['Authorization', 'Content-Type']
CROSSHEADERS_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'e_nursery.urls'

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

WSGI_APPLICATION = 'e_nursery.wsgi.application'



DATABASES = {
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'e_nursery',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
    }
}



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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# for image
STATIC_URL='/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL= '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECURE_REFERRER_POLICY = ''

SECURE_REFERRER_POLICY = 'same-origin'


CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
]


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
       'http://localhost:3000',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # for mail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'enurseryfeuji@gmail.com'
EMAIL_HOST_PASSWORD = 'yttvohlhflzatitu'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False