#!/usr/bin/env bash
#this bash script sets up the webservers for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx start
sudo mkdir data/web_static/shared/
sudo mkdir data/web_static/releases/test/
sudo echo "<html><head></head><body>ALX School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /home/ubuntu/data/web_static/releases/test/ /home/ubuntu/data/web_static/current
sudo chown -R ubuntu:ubuntu data/
sudo sed -i '57 i \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo systemctl reload nginx
