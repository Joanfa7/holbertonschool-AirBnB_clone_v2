#!/usr/bin/env bash
# Bash script that sets up your web servers for the deplyment of web_static.

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
ufw allow 'Nginx HTTP'

sudo mkdir -p  /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo mkdir -p  /data/web_static/shared
sudo echo "Hello World" | tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart

