from .base import *
from .base import env

try:
    SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="-DMIQLNG-I9AetRVHv0HU3UAtT6hX1JL2fReDAyYSNsqPPUO5aE",
)
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


DEBUG = bool(env('DEBUG', default=False))
# DEBUG = False


# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])

if 'POSTGRES_DB' in os.environ:
    DATABASES = {"default": env.db("DATABASE_URL")}
    # DATABASES = {"default": env("DATABASE_URL")}
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}



# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15     # 15 minutes caching
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'mlb'

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SEND_SENT_EVENT = True
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env("CELERY_BACKEND"),
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
    "Access-Control-Allow-Origin"
)



CSRF_TRUSTED_ORIGINS = [
    'https://django.localhost', 
    'https://django.localhost:8011',
    'https://django.localhost:8013'
]


CORS_ORIGIN_WHITELIST = [
    'https://django.localhost',
    'https://django.localhost:8011', 
    'https://django.localhost:8013'
]
CORS_ALLOWED_ORIGINS = [
    'https://django.localhost',
    'https://django.localhost:8011', 
    'https://django.localhost:8013',
    
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# The Security Headers website recommends a minimum value of 2,592,000, equal to 30 days.
SECURE_HSTS_SECONDS = 2_592_000

SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# # Email settings1
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = "support@maina_wanjau.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Mill Bakers"

ADMINS = [("""Maina Wanjau""", "maina.wanjau@gmail.com"),]

MANAGERS = ADMINS

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
            },
            # TODO: remove the below
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue"
            }
        },
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
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
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
