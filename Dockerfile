FROM binkhq/python:3.8

WORKDIR /app

RUN pip install requests flask gunicorn

ADD settings.py .
ADD pingapi.py .
ADD pingproxy.py .
ADD pingclient.py .
