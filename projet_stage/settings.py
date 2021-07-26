"""
Django settings for projet_stage project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7xn(tfva3y0a(y05yk&+%)uk=!_e41_e(ik!ez&ck7i^bx#2l_'

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
    'django_filters',
    'accounts',
    'main',
    'contact',
    'grade_de_travail',
    'lieu_de_travail',
    'agent',
    'migrant_irregulier',
    'operation',
    'fichier_des_operations',
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

ROOT_URLCONF = 'projet_stage.urls'

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

WSGI_APPLICATION = 'projet_stage.wsgi.application'











# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

################################################### les parametres de la bases de donnees ###########################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',     # le sgbd 
        'NAME': 'database_project',       # le nom de la base de donnees 
        'USER':'ghassen',           # le nom de l'utilisateur 
        'PASSWORD':'',              # un mots de passe s'il existe 
        'HOST':'',                  # l'adresse ip 
        'PORT':'5432',              # le port qu'on travail avec 
    }
}
####################################################################################################################################










# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True







# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'




# definir le nouveau modele User avant les modifications
############################################################################################################################
AUTH_USER_MODEL = 'accounts.CustomUser'
############################################################################################################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






##################################### tous les fonctions pour envoyer un mail avec django ############################################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USER_TLS = True
EMAIL_HOST_USER = 'adresse mail du site web'
EMAIL_HOST_PASSWORD = " mots de passe de l'adresse mail "
##################################################################################################################################




######################################### Intialiser les fichiers static pour le design du site web ####################################
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
#########################################################################################################################################
