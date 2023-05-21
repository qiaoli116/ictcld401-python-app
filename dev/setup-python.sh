#!/bin/bash
sudo yum update -y
sudo yum install -y python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install flask
sudo pip3 install mysql-connector-python

