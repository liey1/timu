/etc/init.d/mariadb start
mysql -uroot -proot < /ctf.sql
rm -f /ctf.sql

cd /app
sudo -u www-data /usr/bin/php -S 0.0.0.0:80

tail -f /etc/passwd

