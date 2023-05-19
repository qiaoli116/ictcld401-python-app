#!/bin/bash

# Install required packages
sudo yum update -y
sudo yum install -y openssh-server

# Configure SSH server for SFTP
sudo sed -i 's/^#Subsystem      sftp    .*/Subsystem      sftp    internal-sftp/' /etc/ssh/sshd_config
echo 'Match User ec2-user' | sudo tee -a /etc/ssh/sshd_config
echo '    ChrootDirectory /home/ec2-user' | sudo tee -a /etc/ssh/sshd_config
