from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%$47*h)7l*68u!^i^n$0k4$)wc9kbstwwowl)x54rzbf84mo4m'


# try:
#     SECRET_KEY = env("SECRET_KEY")
# except KeyError as e:
#     raise RuntimeError("Could not find a SECRET_KEY in environment") from e


DEBUG = True

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
ALLOWED_HOSTS = ['localhost','django.localhost','site.millbakers.duckdns.org', '192.168.100.2','127.0.0.1','*.eu-west-1.elasticbeanstalk.com','*.elasticbeanstalk.com','uat-sfc-tracker-v4.eu-west-1.elasticbeanstalk.com']



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
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

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

CSRF_TRUSTED_ORIGINS = ['http://site.millbakers.duckdns.org:8005','http://django.localhost', 'http://site.millbakers.duckdns.org:8059', 'http://127.0.0.1:8005', 'http://127.0.0.1:8059']


CORS_ORIGIN_WHITELIST = [
    "http://localhost:8005",
    "http://django.localhost:8000",
    "http://localhost:8059",
    "http://site.millbakers.duckdns.org:8005",
    "http://site.millbakers.duckdns.org:8059",
    "http://127.0.0.1:8059",
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8005",
    "http://django.localhost:8000",
    "http://localhost:8059",
    "http://site.millbakers.duckdns.org:8005",
    "http://site.millbakers.duckdns.org:8059",
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


CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "Africa/Nairobi"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"


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