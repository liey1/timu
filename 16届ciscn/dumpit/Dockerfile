FROM liey/mariadb10

# RUN apt update -y
# RUN apt install -y mariadb-server mariadb php php-mysql

# RUN apt install -y software-properties-common

RUN apt install -y sudo 

RUN chmod +s /usr/bin/mariadb-dump



COPY ctf.sql /
COPY start.sh /

COPY flag /
RUN chmod 000 /flag

RUN mkdir /app
RUN mkdir /app/log
RUN chmod 777 /app/log
COPY index.php /app/

ENTRYPOINT cd /; /start.sh

EXPOSE 80