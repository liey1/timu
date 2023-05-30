FROM python:3.9.3-slim-buster

RUN python3 -m pip install flask

COPY start.sh /

COPY main /
COPY flag /

RUN mkdir /app
COPY app/server.py /app/server.py

ENTRYPOINT cd /; /start.sh

EXPOSE 80