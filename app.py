from flask import Flask, render_template
import requests
import configparser

def loadConfiguration():
    config = configparser.ConfigParser()
    config.read('./config.ini')  # Replace 'config.ini' with the path to your configuration file
    return config

# Obtain a session token
def obtainSessionToken():
    # Obtain a session token from the metadata service
    TOKEN_URL = 'http://169.254.169.254/latest/api/token'
    TOKEN_TTL = '21600'
    TOKEN_HEADER = {'X-aws-ec2-metadata-token-ttl-seconds': TOKEN_TTL}
    token_response = requests.put(TOKEN_URL, headers=TOKEN_HEADER)
    session_token = token_response.text
    return session_token

# Retrieve the private IP address using the session token
def retrivePrivateIP():
    session_token = obtainSessionToken()
    # Retrieve the private IP address using the session token
    PRIVATE_IP_URL = 'http://169.254.169.254/latest/meta-data/local-ipv4'
    IP_HEADER = {'X-aws-ec2-metadata-token': session_token}
    ip_response = requests.get(PRIVATE_IP_URL, headers=IP_HEADER)
    private_ip = ip_response.text
    return private_ip

app = Flask(__name__)


@app.route('/')
def index():
    private_ip = retrivePrivateIP()
    message = {'private_ip': private_ip}
    return render_template('index.html', message=message)

if __name__ == '__main__':
    # Call the function to load the configuration
    config = load_configuration()

    host = config.get('Server', 'host', fallback="0.0.0.0") 
    port = config.getint('Server', 'port', fallback=8080)  

    # run the http server with port 8080
    app.run(host=host, port=port)
