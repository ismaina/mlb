from .base import *

try:
    SECRET_KEY = env("SECRET_KEY")
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

DEBUG = False

USE_X_FORWARDER_HOST = True
USE_X_FORWARDER_PORT = True
ALLOWED_HOSTS = ['site.millbakers.duckdns.org', 'site.local' ,'*.millbakers.duckdns.org','localhost', '192.168.100.2','127.0.0.1' '192.168.100.2','127.0.0.1', '10.19.130.90']
# ALLOWED_HOSTS = ['site.local','*.millbakers.duckdns.org','millbakers.duckdns.org','site.millbakers.duckdns.org','*.eu-west-1.elasticbeanstalk.com','*.elasticbeanstalk.com','uat-sfc-site-v5-dev.eu-west-1.elasticbeanstalk.com']

X_FRAME_OPTIONS= 'SAMEORIGIN'


CORS_ORIGIN_WHITELIST = [
    "https://10.19.130.90",
    "https://site.local",
    "https://site.millbakers.duckdns.org",
    "http://site.millbakers.duckdns.org",
    "https://172.19.0.*",
    "https://site.local:8090",
]

CORS_ALLOWED_ORIGINS = [
    "https://10.19.130.90",
    "https://site.local",
    "http://site.millbakers.duckdns.org",
    "https://site.millbakers.duckdns.org",
    "https://172.19.0.*",
    "https://site.local:8090",
]


CSRF_TRUSTED_ORIGINS = ['https://site.mwanjau.duckdns.org', 'https://10.19.130.90', 'https://site.mwanjau.duckdns.org','http://*.site.local','https://*site.local', 'https://172.19.0.*', 'https://127.0.0.1', 'https://*.127.0.0.1']
# CSRF_TRUSTED_ORIGINS = ['https://uat-sfc-site-v3.eu-west-1.elasticbeanstalk.com','http://uat-sfc-site-v3.eu-west-1.elasticbeanstalk.com','https://*.127.0.0.1','http://*.127.0.0.1']


CORS_ALLOW_HEADERS = ['*']
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 2_592_000  # 30 days

SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ADMINS = [("""Maina Wanjau""", "maina.wanjau@gmail.com"),]

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Maina Wanjau <maina.wanjau@gmail.com>",
)

SITE_NAME = "Mill Bakers"
# # Email settings1
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'agripmart@gmail.com'
EMAIL_HOST_PASSWORD = 'xsvwohyiyyszcbro'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Millbakers Website]",
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}