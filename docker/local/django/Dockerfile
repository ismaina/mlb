# ARG PYTHON_VERSION=3.10-slim-buster
# ARG PYTHON_VERSION=python3.11-nodejs20-slim
ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local
# ENV http_proxy "http://proxy2.safaricom.net:8080"
# ENV https_proxy "http://proxy2.safaricom.net:8080"
# ENV HTTPS_PROXY="http://proxy2.safaricom.net:8080"
# ENV HTTP_PROXY="http://proxy2.safaricom.net:8080"


RUN apt-get update && apt-get install --no-install-recommends -y \
   iputils-ping \
   build-essential \
   curl \
   python3-six \
   # for psycopg2 
   libpq-dev 

COPY ./requirements/ .

RUN pip install --upgrade pip
RUN pip install six
RUN pip wheel --wheel-dir /usr/src/app_local/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


# CMD ["npm","-v"]
# CMD ["node","-v"]

# RUN npm install -g node@latest

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app_local
# prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# python output is transmitted directly to terminal without being buffered
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN mkdir ssl

RUN mkdir ssl/cert/ 

RUN mkdir ssl/key/

RUN mkdir staticfiles/


# RUN apt-get update && apt-get install --no-install-recommends -y \
#     && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#     && rm -rf /var/lib/apt/lists/*
# ENV http_proxy "http://proxy2.safaricom.net:8080"
# ENV https_proxy "http://proxy2.safaricom.net:8080"
# ENV HTTPS_PROXY="http://proxy2.safaricom.net:8080"
# ENV HTTP_PROXY="http://proxy2.safaricom.net:8080"

# create the app user
# RUN addgroup --system django && adduser --system --group django

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext netcat \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


COPY --from=python-build-stage /usr/src/app_local/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# COPY ./docker/local/django/start_tailwind /start_tailwind
# RUN sed -i 's/\r$//g' /start_tailwind
# RUN chmod +x /start_tailwind

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# COPY --chown=django:django . ${APP_HOME}
COPY . ${APP_HOME}

CMD ["ls","-","al"]

# RUN mkdir /app_local/staticfiles/

# RUN chmod -R 755 /app_local/
RUN chmod -R 755 /app_local/staticfiles/

# USER django

ENTRYPOINT ["/entrypoint"]