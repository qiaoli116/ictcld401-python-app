# Flask Web App
This is a simple Flask web application that displays information on the AWS EC2 server. Note this app must be running on an AWS EC2 server.

## Getting Started
To run the app, you must have Python 3.x and the Flask library installed on your system. You can install Flask using pip by running the following command:

```bash
pip install Flask
```

Once you have installed Flask, you can run the app using the following command:

```bash
python app.py
```
The application will be listening to port **8080** by default.

You may also configure EC2 user data with the following code
```bash
#!/bin/bash
sudo yum update -y
sudo yum install -y git
sudo yum install -y python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install flask
cd /home/ec2-user/
wget --output-document=python-app.zip https://github.com/qiaoli116/ictcld401-python-app/archive/refs/heads/session-3-branch.zip
unzip python-app.zip
mv ictcld401-python-app-session-3-branch python-app

# Modify the configuration file as you need below. Here is an example
# cd /home/ec2-user/python-app/
# sed -i 's/^port\s*=\s*.*/port = 8000/' config.ini

sudo tee /etc/systemd/system/my_python_app.service <<EOF
[Unit]
Description=My Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user
ExecStart=/usr/bin/python3 /home/ec2-user/python-a
/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start my_python_app.service
sudo systemctl enable my_python_app.service
```

This will start the Flask development server, and the app will be accessible in your web browser at http://&lt;domain&gt;:8080/.

## Configure the server
When command **python app.py** is executed, the Flask web server is started using the configuration defined in the **config.ini** file, which has the following default content.
```ini
[Server]
host = 0.0.0.0
port = 8080
```
To apply custom configuration, you need to modify this file before launching the Flash web server. You may use one of the following method to update this file.
 - using text editor, such as vi, vim or nano.
 - using **sed** command. For example, to use port 8000, you could run **sed -i 's/^port\s*=\s*.*/port = 8000/' config.ini**. You may add this **sed** command to the EC2 user data, after the program is downloaded and extracted, to start the server using a different port number.

```bash
# more code
wget --output-document=python-app.zip https://github.com/qiaoli116/ictcld401-python-app/archive/refs/heads/session-3-branch.zip
unzip python-app.zip
mv ictcld401-python-app-session-3-branch python-app

# modify the config.ini if needed. the following example changed the port number to 8000
cd /home/ec2-user/python-app/
sed -i 's/^port\s*=\s*.*/port = 8000/' config.ini

sudo tee /etc/systemd/system/my_python_app.service
# more code
```

## Checking the Result
If the app runs correctly, you should see a web page displayed in your web browser.

## Contact
If you have any questions about this project, feel free to contact me at <qiao.li@holmesglen.edu.au>.

## License
This project is licensed under the MIT License.