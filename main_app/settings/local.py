from .base import *


DEBUG = True
ALLOWED_HOSTS = ['localhost','django.localhost', '192.168.100.2','127.0.0.1','*.eu-west-1.elasticbeanstalk.com','*.elasticbeanstalk.com','uat-sfc-tracker-v4.eu-west-1.elasticbeanstalk.com']

# X_FRAME_OPTIONS= 'SAMEORIGIN'
CORS_ALLOW_HEADERS = ['*']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    "django.localhost",
    # ...
]

CSRF_TRUSTED_ORIGINS = ['http://django.localhost:8005', 'http://django.localhost:8059', 'http://127.0.0.1:8005', 'http://127.0.0.1:8059']


CORS_ORIGIN_WHITELIST = [
    "http://localhost:8005",
    "http://localhost:8059",
    "http://django.localhost:8005",
    "http://django.localhost:8059",
    "http://127.0.0.1:8059",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "http")

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 60

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