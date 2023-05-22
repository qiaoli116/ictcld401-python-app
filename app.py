from flask import Flask, render_template, jsonify
from lib.config import load_configuration
from models.ec2_instance import EC2Instance, EC2Self
from app_config import app_config 

###################### Main ######################

# Create a Flask app
app = Flask(__name__)

# generate the data for the / page and api/
def indexData():
    ec2_self = EC2Self()
    data = {
        'ec2_self': ec2_self.to_list(),
        'static_base_url': app_config.static_config.base_url if app_config.static_config.is_base_url_up() else None,
    }
    print(data)
    return data

# Route to handle the landing page
@app.route('/')
def index():
    return render_template('index.html', data=indexData())

# Route to handle the api page
@app.route('/api')
def api():
    return jsonify(indexData())

if __name__ == '__main__':
    # Call the function to load the configuration
    config = load_configuration()

    # run the http server with port 8080
    app.run(host=app_config.server_config.host, port=app_config.server_config.port)
