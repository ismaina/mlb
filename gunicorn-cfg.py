# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Maina Wanjau
"""

bind = '0.0.0.0:8005'
workers = 4
accesslog = '-'
loglevel = 'debug'
enable_stdio_inheritance = True
# Restart workers when code changes (development only!)
reload = True

# Write access and error info to /var/log
# accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True

# daemon = True