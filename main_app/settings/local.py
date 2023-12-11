from .base import *
from .base import env

try:
    SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="-DMIQLNG-I9AetRVHv0HU3UAtT6hX1JL2fReDAyYSNsqPPUO5aE",
)
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


# DEBUG = bool(env('DEBUG', default=True))
DEBUG = True

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
ALLOWED_HOSTS = ['localhost','django.localhost','caribou-sweet-wallaby.ngrok-free.app']

# ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])

if 'POSTGRES_DB' in os.environ:
    # DATABASES={
    #     'default':{
    #         'ENGINE':'django.db.backends.postgresql',
    #         'NAME':env('POSTGRES_DB'),
    #         'USER':env('POSTGRES_USER'),
    #         'PASSWORD':env('POSTGRES_PASSWORD'),
    #         'HOST':env('POSTGRES_HOST'),
    #         'PORT':env('POSTGRES_PORT'),
    #     }
    # }
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
)

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    "django.localhost",
    # ...
]

CSRF_TRUSTED_ORIGINS = ['https://site.millbakers.duckdns.org','http://django.localhost', 'http://django.localhost:8001']


CORS_ORIGIN_WHITELIST = [
    "http://localhost:8005",
    "http://django.localhost:8001",
    "http://localhost:8059",
    "https://site.millbakers.duckdns.org",
    "https://site.millbakers.duckdns.org:8005",
    "https://site.millbakers.duckdns.org:8059",
    "http://millbakers.duckdns.org:8001",
    "http://127.0.0.1:8059",
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8005",
    "http://django.localhost:8001",
    "http://localhost:8059",
    "https://site.millbakers.duckdns.org",
    "https://site.millbakers.duckdns.org:8005",
    "https://site.millbakers.duckdns.org:8059",
    "http://millbakers.duckdns.org:8001",
    "http://127.0.0.1:8059",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "http")

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 30

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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'agripmart@gmail.com'
EMAIL_HOST_PASSWORD = 'xsvwohyiyyszcbro'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = "support@maina_wanjau.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Mill Bakers"

ADMINS = [("""Maina Wanjau""", "maina.wanjau@gmail.com"),]

MANAGERS = ADMINS

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
#             "%(process)d %(thread)d %(message)s"
#         }
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         }
#     },
#     "root": {"level": "INFO", "handlers": ["console"]},
# }
# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}