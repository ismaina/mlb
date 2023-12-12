# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Maina Wanjau
"""
import multiprocessing
# import ssl    

chdir="/app_local"
# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "main_app.wsgi:application"
# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1
# The socket to bind
bind = '0.0.0.0:8000'
keyfile= "/ssl/mysite.key"
certfile= "/ssl/mysite.crt"

# Restart workers when code changes (development only!)
reload = True
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = 'debug'
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/prod.pid"
# Redirect stdout/stderr to log file
capture_output = True
# Daemonize the Gunicorn process (detach & enter background)
# daemon = True
# cert_reqs = ssl.CERT_REQUIRED
# ssl_version = ssl.PROTOCOL_TLSv1_2