ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production

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
RUN pip wheel --wheel-dir /usr/src/app_production/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


# CMD ["npm","-v"]
# CMD ["node","-v"]

# RUN npm install -g node@latest

FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app_production
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


RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext netcat \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


COPY --from=python-build-stage /usr/src/app_production/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

COPY ./docker/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/production/django/start_prod /start_prod
RUN sed -i 's/\r$//g' /start_prod
RUN chmod +x /start_prod

# COPY ./docker/production/django/start_tailwind /start_tailwind
# RUN sed -i 's/\r$//g' /start_tailwind
# RUN chmod +x /start_tailwind

COPY ./docker/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# COPY --chown=django:django . ${APP_HOME}
COPY . ${APP_HOME}

CMD ["ls","-","al"]

# RUN mkdir /app_production/staticfiles/

# RUN chmod -R 755 /app_production/
RUN chmod -R 755 /app_production/staticfiles/

# USER django

ENTRYPOINT ["/entrypoint"]