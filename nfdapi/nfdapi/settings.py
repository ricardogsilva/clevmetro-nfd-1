"""
Django settings for nfdapi project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPGroupQuery,\
    PosixGroupType
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = '/var/www/media'
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# we need to run django-admin collectstatic whenever dependences are modified or updated
STATIC_ROOT = '/var/www/clevmetronfd-static'
STATIC_URL = '/nfdapi-static/'


#APP_NAME = ""
#APP_NAME = "/"
APP_NAME = "nfdapi/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9TcxXNZfyPAcWZaOc8aOlvwJ6pG0te1DlAQpkCz3L7SvNKx3xSLK7CkegPDxzySbNwL8pPO8M0TZxuuuf2jQ09iJ3ytdQ5VuTa0vrIhxBBGssVTHXhvCqHEPd5L2JccH'
#SECRET_KEY = 'c6s_pn$c%e4+x!318(+yapf8s)j8^e3u1j&u9kq)&9x1l_a45i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'nfdusers.user'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'reversion',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'rest_auth',
    'nfdcore',
    'nfdusers',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nfdapi.urls'

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

WSGI_APPLICATION = 'nfdapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'metroparksnfd',
        'USER': 'metroparksnfd',
        'PASSWORD': 'metroparksnfd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
    
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # it's very important to set first the TokenAuthentication because otherwise
        # the mobile apps fail to authenticate
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'nfdcore.jwtutils.jwt_response_payload_handler',
    'JWT_ALLOW_REFRESH': True,
    #'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    #'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=10),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=10),
    #'JWT_AUTH_COOKIE': 'nfdjwtauth'
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
"""
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
"""

# We are using AD/LDAP passwords, so we rely on their corporative validation rules
AUTH_PASSWORD_VALIDATORS = [
]

AUTH_LDAP_SERVER_URI = "ldap://localhost:389"


"""
Configuration for OpenLDAP
"""
AUTH_LDAP_BIND_DN = "cn=admin,dc=nfd,dc=geo-solutions,dc=it"
AUTH_LDAP_BIND_PASSWORD = "1geosolutions2"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=nfd,dc=geo-solutions,dc=it",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")


AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    ldap.SCOPE_SUBTREE
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300
AUTH_LDAP_MIRROR_GROUPS = True

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=nfdadmins,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_superuser": "cn=nfdadmins,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_plant_writer": "cn=plant_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_plant_publisher": "cn=plant_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_animal_writer": "cn=animal_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_animal_publisher": "cn=animal_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_slimemold_writer": "cn=slimemold_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_slimemold_publisher": "cn=slimemold_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_fungus_writer": "cn=fungus_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_fungus_publisher": "cn=fungus_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_naturalarea_writer": "cn=naturalarea_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_naturalarea_publisher": "cn=naturalarea_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it"
}

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "cn",
    "last_name": "sn",
    "email": "mail"
}

"""
Configuration for Active Directory:
"""
"""
AUTH_LDAP_BIND_DN = "cn=Bind_User,ou=Users,dc=nfd,dc=geo-solutions,dc=it"
AUTH_LDAP_BIND_PASSWORD = "kwNw8iqzr9p"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Users,dc=nfd,dc=geo-solutions,dc=it",
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")


AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,dc=nfd,dc=geo-solutions,dc=it",
    ldap.SCOPE_SUBTREE, "(objectClass=group)")
)
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=nfdadmins,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_superuser": "cn=nfdadmins,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_plant_writer": "cn=plant_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_plant_publisher": "cn=plant_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_animal_writer": "cn=animal_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_animal_publisher": "cn=animal_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_slimemold_writer": "cn=slimemold_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_slimemold_publisher": "cn=slimemold_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_fungus_writer": "cn=fungus_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_fungus_publisher": "cn=fungus_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_naturalarea_writer": "cn=naturalarea_writer,ou=groups,dc=nfd,dc=geo-solutions,dc=it",
    "is_naturalarea_publisher": "cn=naturalarea_publisher,ou=groups,dc=nfd,dc=geo-solutions,dc=it"
}

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

"""


#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=nfdusers,dc=nfd,dc=geo-solutions,dc=it"
#AUTH_LDAP_START_TLS = True

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
  ('en', _('English'))
]
LOCALE_PATHS = [
    BASE_DIR + '/nfdcore/locale',
    BASE_DIR + '/locale',
]
print LOCALE_PATHS


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

"""
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django_auth_ldap': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 1,
    ldap.OPT_REFERRALS: 0,
}
"""
