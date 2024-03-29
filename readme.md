# Flask Web App
This is a simple Flask web application that displays information of the web server, including
 - Current EC2 instance information
 - S3 static server information
 - All EC2 instances information
Note this app must be running on an AWS EC2 server; optionally an S3 bucket can be configured as static content server and a RDS MySQL can be configured to store information of EC2 instance.

## Getting Started

### Host the application
To run the app, you must have Python 3.x and the pip library installed on your system. Run the following commands to install all required python dependencies:

```bash
sudo yum update -y
sudo yum install -y python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install flask
sudo pip3 install mysql-connector-python
```

After the dependencies are installed, start the app using the following command:

```bash
python3 app.py
```
The application will be listening to port **8080** by default.

This will start the Flask development server, and the app will be accessible in your web browser at http://&lt;domain&gt;:8080/.

By default, the app will start without static content server and database configured. Refer to the [Configure the app](#configure-the-app) section below to understand how to configure the app.

### Host static files in a S3 bucket
A static content server build using AWS S3 bucket linked to this web app. All files inside the ./static folder must be uploaded to the bucket, with file name as the object key value.

The base URL of the static files must be configured in this web app. Refer to the [Configure the app](#configure-the-app) below to understand how to configure static content server.

### Create a database
An RDS mysql databse must be created and accessible to the app EC2 servers.

The following information must be configured.
 - endpoint
 - port
 - username
 - password

Refer to the [Configure the app](#configure-the-app) below to understand how to configure the app.

## Configure the app
When command **python app.py** is executed, the Flask web server is started using the configuration defined in the **config.ini** file, which has the following default content.
```ini
[Server]
host = 0.0.0.0
port = 8080

[Static]
base_url = none

[Database]
endpoint = none
port = 3306
user = 
password = 
database = python_web_app
table = ec2_servers
```
To apply custom configuration, you need to modify this file before launching the Flash web server. You may use one of the following method to update this file.
 - using text editor, such as vi, vim or nano.
 - run **python3 setup.py** script to do the configuration
 - run **python3 setup.py --section x --field y --value z** to set field "y" in section "x" to value "z". For example **python3 setup.py --section Server --field port --value 8000** will set the port field under section Server to vaule 8000

After you changed the configuration, the app must be restarted.

## EC2 user data
You may configure EC2 user data with the following code. You must confige the config.ini file with S3, databse information correctly in the script.
Note: you must uncomment and modify the **python3 setup.py** statements below
```bash
#!/bin/bash
sudo yum update -y
sudo yum install -y python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install flask
sudo pip3 install mysql-connector-python
cd /home/ec2-user/
wget --output-document=python-app.zip https://github.com/qiaoli116/ictcld401-python-app/archive/refs/heads/main.zip
unzip python-app.zip
mv ictcld401-python-app-main python-app

# Uncomment and modify the configuration file with correct values
cd /home/ec2-user/python-app
# python3 setup.py --section Static --field base_url --value <base url string>
# python3 setup.py --section Database --field endpoint --value <endpoint string>
# python3 setup.py --section Database --field port --value <default is 3306>
# python3 setup.py --section Database --field user --value <database user name>
# python3 setup.py --section Database --field password --value <database password>

sudo tee /etc/systemd/system/my_python_app.service <<EOF
[Unit]
Description=My Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/python-app
ExecStart=sudo /usr/bin/python3 /home/ec2-user/python-app/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start my_python_app.service
sudo systemctl enable my_python_app.service
```

## Checking the Result
If the app runs correctly, you should see a web page displayed in your web browser.

## Contact
If you have any questions about this project, feel free to contact me at <qiao.li@holmesglen.edu.au>.

## License
This project is licensed under the MIT License.
