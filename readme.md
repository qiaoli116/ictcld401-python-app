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

You may also configure EC2 user data with the following code
```bash
#!/bin/bash
sudo yum update -y
sudo yum install -y git
sudo yum install -y python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install flask
cd /home/ec2-user
rm -r /home/ec2-user/ictcld401-python-app
git clone https://github.com/qiaoli116/ictcld401-python-app.git

sudo tee /etc/systemd/system/my_python_app.service <<EOF
[Unit]
Description=My Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user
ExecStart=/usr/bin/python3 /home/ec2-user/ictcld401-python-app/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start my_python_app.service
sudo systemctl enable my_python_app.service
```

This will start the Flask development server, and the app will be accessible in your web browser at http://domain:8080/.

## Checking the Result
If the app runs correctly, you should see a web page displayed in your web browser.

## Contact
If you have any questions about this project, feel free to contact me at <qiao.li@holmesglen.edu.au>.

## License
This project is licensed under the MIT License.