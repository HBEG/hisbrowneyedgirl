"""
Django settings for hbeg project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file.


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "134.209.156.80",
    "hisbrowneyedgirl.com",
    "www.hisbrowneyedgirl.com",
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#              'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "django.contrib.sites",  # make sure sites is included
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.discord",  # for discord login
    "django_crontab",  # for crontab
    "core.apps.CoreConfig",
    "accounts.apps.AccountsConfig",
    "profiles.apps.ProfilesConfig",
    "public.apps.PublicConfig",
    "simplestorystorage.apps.SimplestorystorageConfig",
    "honeysuckleAPI.apps.HoneysuckleapiConfig",
    # sections
    "sections",
    "sections.harmony",
    "sections.hhrauthors",
    # extras from externals
    "storages",
    "ckeditor",
    "django_filters",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hbeg.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hbeg.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "hbegproject",
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "",
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # existing backend (for admin)
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AUTH URLs and MODEL NAME

LOGIN_REDIRECT_URL = "profile"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "login"

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = "nickname"
ACCOUNT_USERNAME_REQUIRED = True

AUTH_USER_MODEL = "accounts.Member"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

MEDIA_URL = "/images/"

STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = os.path.join(BASE_DIR, "static/images/")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# INSERT FROM hide/aws_cred.txt
# -----------AWS S3 Settings-------------------------------------------------------
# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_FILE_OVERWRITE = False

# AWS_LOCATION = 'static'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATIC_URL = 'https://%s/%s/static/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# # MEDIA_URL = 'https://%s/%s/images/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

# # MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'hbeg.storages.MediaStore'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# THESE ARE FOR CKEDITOR
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline", "-", "Strike", "Subscript", "Superscript"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["RemoveFormat"],
        ],
    },
}
AWS_QUERYSTRING_AUTH = False


# CRON TASKS
CRONJOBS = [
    # run refresh harmony feed every 12 hours
    ("0 */12 * * *", "sections.harmony.cron.feed_ao3_scheduled_job", ">> ~/cron_job.log"),
]
