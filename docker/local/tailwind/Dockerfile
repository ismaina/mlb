ARG PYTHON_VERSION=latest

FROM nikolaik/python-nodejs:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

COPY ./requirements/ .

RUN pip install --upgrade pip
RUN pip install six
RUN pip wheel --wheel-dir /usr/src/app_local/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app_local
# prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# python output is transmitted directly to terminal without being buffered
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}


RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean
# RUN addgroup --system django && adduser --system --group django


WORKDIR ${APP_HOME}/theme/static_src

RUN npm install tailwind kutty flowbite daisyui --save

WORKDIR ${APP_HOME}

COPY --from=python-build-stage /usr/src/app_local/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/


COPY ./docker/local/tailwind/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/tailwind/start_tailwind /start_tailwind
RUN sed -i 's/\r$//g' /start_tailwind
RUN chmod +x /start_tailwind

COPY . ${APP_HOME}

RUN chmod -R 755 /app_local/staticfiles


ENTRYPOINT ["/entrypoint"]