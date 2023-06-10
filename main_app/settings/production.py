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
# ALLOWED_HOSTS = ['site.local','*.millbakers.duckdns.org','millbakers.duckdns.org','site.millbakers.duckdns.org','*.eu-west-1.elasticbeanstalk.com','*.elasticbeanstalk.com','uat-mlb-site-v5-dev.eu-west-1.elasticbeanstalk.com']

X_FRAME_OPTIONS= 'SAMEORIGIN'
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'mlb'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379',
        
    }
}
#  DATABASES AND CACHES
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379),],
        },
    },
}

X_FRAME_OPTIONS= 'SAMEORIGIN'
# CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)


CSRF_TRUSTED_ORIGINS = ['https://site.mwanjau.duckdns.org', 'https://10.19.130.90', 'https://site.mwanjau.duckdns.org','http://*.site.local','https://*site.local', 'https://172.19.0.*', 'https://127.0.0.1', 'https://*.127.0.0.1']
# CSRF_TRUSTED_ORIGINS = ['https://uat-mlb-site-v3.eu-west-1.elasticbeanstalk.com','http://uat-mlb-site-v3.eu-west-1.elasticbeanstalk.com','https://*.127.0.0.1','http://*.127.0.0.1']


CORS_ORIGIN_WHITELIST = [
    "http://localhost:8005",
    "http://django.localhost:8000",
    "http://localhost:8059",
    "https://site.millbakers.duckdns.org",
    "https://site.millbakers.duckdns.org:8005",
    "https://site.millbakers.duckdns.org:8059",
    "http://127.0.0.1:8059",
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8005",
    "http://django.localhost:8000",
    "http://localhost:8059",
    "https://site.millbakers.duckdns.org",
    "https://site.millbakers.duckdns.org:8005",
    "https://site.millbakers.duckdns.org:8059",
    "http://127.0.0.1:8059",
]

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