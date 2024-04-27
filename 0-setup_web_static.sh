#!/usr/bin/env bash
#this bash script sets up the webservers for deployment
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html>
    <head>
        <title>Make it to Server 2</title>
    </head>
    <body>
        <p>Installation Complete</p>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo rm -f /etc/nginx/sites-enabled/default
config_text="server {
    listen 80;
    listen [::]:80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"
echo "$config_text" | sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null
if [ ! -e /etc/nginx/sites-enabled/hbnb_static ]; then
    sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
fi
sudo service nginx restart
