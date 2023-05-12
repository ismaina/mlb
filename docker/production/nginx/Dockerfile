FROM nginx:1.23.0-alpine

ENV http_proxy "http://proxy2.safaricom.net:8080"
ENV https_proxy "http://proxy2.safaricom.net:8080"
ENV HTTPS_PROXY="http://proxy2.safaricom.net:8080"
ENV HTTP_PROXY="http://proxy2.safaricom.net:8080"

RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/default.conf