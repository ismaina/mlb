FROM nikolaik/python-nodejs:latest

USER pn
WORKDIR /home/pn/app
copy --chown=pn:pm . .

RUN pip install -r requirements.txt


EXPOSE 8002
