from flask import Flask, render_template
from lib import loadConfiguration, retrivePrivateIP

###################### Main ######################

# Create a Flask app
app = Flask(__name__)

# Route to handle the landing page
@app.route('/')
def index():
    private_ip = retrivePrivateIP()
    message = {'private_ip': private_ip}
    return render_template('index.html', message=message)


if __name__ == '__main__':
    # Call the function to load the configuration
    config = loadConfiguration()

    host = config.get('Server', 'host', fallback="0.0.0.0") 
    port = config.getint('Server', 'port', fallback=8080)

    static_base_url = config.get('Static', 'static_base_url', fallback="")

    db_endpoint = config.get('Database', 'endpoint', fallback="")
    db_port = config.getint('Database', 'port', fallback=0)
    db_user = config.get('Database', 'user', fallback="")
    db_password = config.get('Database', 'password', fallback="")

    # run the http server with port 8080
    app.run(host=host, port=port)
