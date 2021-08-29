#!/usr/bin/env bash
# sets up web servers for deployment of static website
# Creates the folders where the static resources will be held
# creates placeholder files and symbolic links

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/

printf %s "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By vagrant;
    root /var/www/html;
    index index.html index.htm;
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    error_page 404 /custom_404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
" > /etc/nginx/sites-available/default

service nginx restart
