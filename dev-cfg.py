# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Maina Wanjau
"""

wsgi_app = "main_app.wsgi:application"
bind = '0.0.0.0:8000'
workers = 4
threads = 2
accesslog = errorlog = "/var/log/gunicorn/dev.log"
loglevel = 'debug'
enable_stdio_inheritance = True
# Restart workers when code changes (development only!)

# Write access and error info to /var/log
# accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True

daemon = True