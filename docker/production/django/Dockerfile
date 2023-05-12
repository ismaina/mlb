# ARG PYTHON_VERSION=3.9-slim-bullseye
ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production
ENV http_proxy "http://proxy2.safaricom.net:8080"
ENV https_proxy "http://proxy2.safaricom.net:8080"
ENV HTTPS_PROXY="http://proxy2.safaricom.net:8080"
ENV HTTP_PROXY="http://proxy2.safaricom.net:8080"


RUN apt-get update && apt-get install --no-install-recommends -y \
   iputils-ping \
   build-essential \
   python3-six \
   # for psycopg2 
   libpq-dev 

COPY ./requirements .

RUN pip install --upgrade pip
RUN pip install six
RUN pip wheel --wheel-dir /usr/src/app_prod/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app_prod
# prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# python output is transmitted directly to terminal without being buffered
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN mkdir ssl

RUN mkdir ssl/cert/ 

RUN mkdir ssl/key/
   

# RUN apt-get update && apt-get install --no-install-recommends -y \
#     && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#     && rm -rf /var/lib/apt/lists/*
ENV http_proxy "http://proxy2.safaricom.net:8080"
ENV https_proxy "http://proxy2.safaricom.net:8080"
ENV HTTPS_PROXY="http://proxy2.safaricom.net:8080"
ENV HTTP_PROXY="http://proxy2.safaricom.net:8080"

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext netcat \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app_prod/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

COPY ./docker/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY . ${APP_HOME}


# RUN chmod -R 755 /app_prod/
RUN chmod -R 755 /app_prod/staticfiles

ENTRYPOINT ["/entrypoint"]