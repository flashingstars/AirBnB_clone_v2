#!/usr/bin/env bash
# A script that install and configure nginx

# Updating ubuntu and installing nginx
sudo apt-get update
sudo apt-get install nginx -y

# Creating directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a html page with "Holberton school" as body
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating a symbolic link to connect the directories
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing the directory ownership and permissions
sudo chown -R ubuntu:ubuntu /data/

# Setting up the page to be served to the client on request
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

# Restarting the nginx server
sudo service nginx restart
