from flask import Flask, render_template
from lib.ec2_meta_data import retrive_local_ip, retrive_instance_id, retrive_public_ip
from lib.config import load_configuration

###################### Main ######################

# Create a Flask app
app = Flask(__name__)

# Route to handle the landing page
@app.route('/')
def index():
    local_ip = retrive_local_ip()
    public_ip = retrive_public_ip()
    instance_id = retrive_instance_id()
    message = {
        'local_ip': local_ip,
        'public_ip': public_ip,
        'instance_id': instance_id
    }
    print (message)
    return render_template('index.html', message=message)


if __name__ == '__main__':
    # Call the function to load the configuration
    config = load_configuration()

    host = config.get('Server', 'host', fallback="0.0.0.0") 
    port = config.getint('Server', 'port', fallback=8080)

    static_base_url = config.get('Static', 'static_base_url', fallback="")

    db_endpoint = config.get('Database', 'endpoint', fallback="")
    db_port = config.getint('Database', 'port', fallback=0)
    db_user = config.get('Database', 'user', fallback="")
    db_password = config.get('Database', 'password', fallback="")

    # run the http server with port 8080
    app.run(host=host, port=port)
