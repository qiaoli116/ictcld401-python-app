#!/bin/bash
sudo yum update -y
sudo dnf install mariadb105-server -y
# mysql -h <host> -P <port> -u <username> -p