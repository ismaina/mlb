from .base import *

USE_X_FORWARDER_HOST = True
USE_X_FORWARDER_PORT = True
CSRF_TRUSTED_ORIGINS = ['http://localhost:8005', 'http://localhost:8059', 'http://127.0.0.1:8005', 'http://127.0.0.1:8059']


CORS_ORIGIN_WHITELIST = [
    "http://localhost:8005",
    "http://localhost:8059",
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

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ADMINS = [("""Maina Wanjau""", "mwanjau@safaricom.co.ke"),("""eisp""", "enterpriseprogrammability@Safaricom.co.ke")]
ADMINS = [("""Maina Wanjau""", "mwanjau@safaricom.co.ke"),("""Daniel Otieno""", "dootieno@safaricom.co.ke"), ("""Sydney Waithaka""", "swanjohi@safaricom.co.ke")]

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Maina Wanjau <mwanjau@safaricom.co.ke>",
)

SITE_NAME = "Project names"

SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Safaricom Project name]",
)