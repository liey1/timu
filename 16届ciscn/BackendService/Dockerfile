FROM nacos/nacos-server:2.0.2

COPY start.sh /

COPY backend-1.0-SNAPSHOT.jar /
COPY flag /

ENTRYPOINT cd /; /start.sh

EXPOSE 80