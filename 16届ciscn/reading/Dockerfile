FROM python:3.9.3-slim-buster

RUN python3 -m pip install flask

COPY start.sh /
RUN mkdir /app
COPY app /app
COPY flag /


ENTRYPOINT cd /; /start.sh

EXPOSE 8000