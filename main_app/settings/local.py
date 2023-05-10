from .base import *

ALLOWED_HOSTS = ['localhost', '192.168.100.2','127.0.0.1','*.eu-west-1.elasticbeanstalk.com','*.elasticbeanstalk.com','uat-sfc-tracker-v4.eu-west-1.elasticbeanstalk.com']



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