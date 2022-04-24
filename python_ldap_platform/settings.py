"""
Django settings for python_ldap_platform project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import configparser
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'online.conf'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q6_$-_=g$*yp(uc#n6usxl%bd8uu2nk5=0svcp0h9#q@&z5ncf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_COOKIE_NAME = 'python_ldap_platform'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 24  # 24小时
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'python_ldap_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'python_ldap_platform.views.global_setting'
            ],
        },
    },
]

WSGI_APPLICATION = 'python_ldap_platform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data/db.sqlite3',
    }
}

# 使用mysql数据库
# DB_HOST = config.get('db', 'host')
# DB_PORT = config.getint('db', 'port')
# DB_USER = config.get('db', 'user')
# DB_PASSWORD = config.get('db', 'password')
# DB_DATABASE = config.get('db', 'database')
# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': DB_DATABASE,
#             'USER': DB_USER,
#             'PASSWORD': DB_PASSWORD,
#             'HOST': DB_HOST,
#             'PORT': DB_PORT,
#     }
# }


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
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

#LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# HTML中使用的静态文件夹前缀
STATIC_URL = '/static/'

# 静态文件存放位置
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '%(asctime)s %(message)s'},
        'standard': {
            'format': '%(asctime)s  [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/default.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        'details_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'details': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/details.log',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 10,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        'details_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/details_error.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'default', 'error'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['console', 'default', 'error'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django.db.backends': {
            'handlers': ['default'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'sso': {
            'handlers': ['details_console', 'details', 'details_error'],
            'propagate': True,
            'level': 'DEBUG',
        }

    }
}

AUTH_USER_MODEL = 'accounts.User'


LOGIN_URL = "/login"
_LOGIN_URL = "/login"
_DEFAULT_FORWARD = '/'
_TICKET_NAME = "ticket"
_TIME_OUT = 9000

_REDIS_HOST = config.get('redis', 'host')
_REDIS_PORT = config.get('redis', 'port')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_PORT = config.get('email', 'EMAIL_PORT')
EMAIL_USE_SSL = config.get('email', 'EMAIL_USE_SSL')
#发送邮件的邮箱
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
#收件人看到的发件人
EMAIL_FROM = config.get('email', 'EMAIL_FROM')


PUBKEY = """
-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBANV2wprstJN44AmccNpD1Mc5sQs+bdPJsUvB/UYmyEJiQbaU90g93+5P
VS1P6d6SvzwXsiPRXP8GWCYduZPt+Bb/FXYcipDl0WBDm/d/unrtXrF59TERlXoG
qIAV5hfFKKw5deWSKDrDtP+cVIOhouvju05eYI6Qg4pDpEsJgyWRAgMBAAE=
-----END RSA PUBLIC KEY-----
"""

PRIVKEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICYgIBAAKBgQDVdsKa7LSTeOAJnHDaQ9THObELPm3TybFLwf1GJshCYkG2lPdI
Pd/uT1UtT+nekr88F7Ij0Vz/BlgmHbmT7fgW/xV2HIqQ5dFgQ5v3f7p67V6xefUx
EZV6BqiAFeYXxSisOXXlkig6w7T/nFSDoaLr47tOXmCOkIOKQ6RLCYMlkQIDAQAB
AoGBAMBhX9GwMq4V6hO/YhXTvBgw7lZr1R9iTt8v3cszeJgbZY3fg10gJojoBqPn
uaZWKvNFh86wCVftp9PyRUCkfpOko8vLaSjwIcXoW3mYQ5I4+lXLe5Ygg37YfbBp
Khft2ixU4MoINS4X23HWGG6gA0oV+pXUUvvFo9nHFZiLyySBAkUA/oK5mzIF0kab
mMdlDn+sW+qCcDRxDgTk+9y1oMhZn4PgSw+UH2L6vMy+wCGmjfZoMG5Bp358ZIR9
ooL9Kb1SzPUquu0CPQDWtotSvQDsByBPQ0qBdcz9wRCQPULmbzmpbDYKDT2dYzFk
HKTbvirjme8q2qsPOEn8GF0jfRVjEu4VbLUCRQCpcn2CfzZy/kF/4Vk94vDtLV/0
tmWC0O1nZlWim2FYG6QMNW4Hy41mf+aL4puSLrjFbdLWYhcNkUxYE1/cF0l2XdA6
LQI8DlwQ/0ySpjZny8VFU1ksh4AE+pCOS9j+cz1Ac/WkvETpBbgAso2KUsR1wVj0
fcUW9ZwvhnMUHhcjAx3NAkUA+8AU7oxTxyKe2izoNu0cnOPglCN/kQasqZ6QeOx1
MVX0zMCP+m5Mp7jrDnZIG1fT/jVuzkbQed9WhofpYv3R6zzKo1w=
-----END RSA PRIVATE KEY-----
"""

DOMAIN_NAME = config.get('base', 'DOMAIN_NAME')
SITE_NAME = config.get('base', 'SITE_NAME')
DOMAIN_SUFFIX = config.get('ldap', 'DOMAIN_SUFFIX')
EXT_PER = config.get('base', 'external_permission')

# jenkins配置
JENKINS_URL = config.get('jenkins', 'JENKINS_URL')
JENKINS_USERNAME = config.get('jenkins', 'JENKINS_USERNAME')
JENKINS_PASSWORD = config.get('jenkins', 'JENKINS_PASSWORD')


# Yearning配置
Y_HOST = config.get('yearning', 'host')
Y_PORT = config.getint('yearning', 'port')
Y_USER = config.get('yearning', 'user')
Y_PASSWORD = config.get('yearning', 'password')
Y_DATABASE = config.get('yearning', 'database')


# aly配置
ACCESS_ID = config.get('aliyun', 'access_id')
ACCESS_KEY = config.get('aliyun', 'access_key')
ACCOUNT_MAIL = config.get('aliyun', 'accout_mail')











