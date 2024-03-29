from flask import Flask, render_template, jsonify, request
from models.ec2_instance import EC2Instance, EC2Self
#from app_config import app_config 
from models.db import AppDAL
from models.ec2_instance import EC2DBItem
from models.ec2_meta_data import EC2MetaData
import json
import random
import string

from models.config import AppConfig 
app_config = AppConfig("config.ini")

###################### Main ######################

# Create a Flask app
app = Flask(__name__)

# todo - move this function to somewhere else
def app_init_create_or_update_item():
    app_dal = AppDAL(
            host=app_config.db_config.endpoint,
            port=app_config.db_config.port,
            user=app_config.db_config.user,
            password=app_config.db_config.password,
            database=app_config.db_config.database,
            table=app_config.db_config.table
        )
    app_dal.connect_to_sql_server()
    if app_dal.is_sql_server_connected() is True:
        print("app.py - Sql server is connected")
        if app_dal.connect_to_db() is True:
            print("app.py - Database is connected")
        else:
            print("app.py - Failed to connect to the database, init it")
            if app_dal.init_db() is True:
                print("app.py - Database initialized successfully")
            else:
                print("app.py - Failed to initialize the database")
    else:
        print("app.py - Failed to connect to the sql server")

    if app_dal.connect_to_db() is True:
        # create the item for current instance
        item = EC2DBItem(
                instance_id=EC2MetaData.retrive_instance_id(),
                local_ip=EC2MetaData.retrive_local_ip(),
                public_ip=EC2MetaData.retrive_public_ip(),
                app_port=app_config.server_config.port,
            )
        # create the item for current instance in db
        print("app.py - create or update the item for current instance in db")
        app_dal.create_or_update(item.instance_id, json.dumps(item.to_dict_db()))
    app_dal.close_connection()

# todo - split and move this function to somewhere else
# generate the data for the / page and api/
def indexData():
    ec2_servers = {
        "db_connected": False,
        "servers": None
    }
    print(ec2_servers)
    app_dal = AppDAL(
            host=app_config.db_config.endpoint,
            port=app_config.db_config.port,
            user=app_config.db_config.user,
            password=app_config.db_config.password,
            database=app_config.db_config.database,
            table=app_config.db_config.table
        )
    app_dal.connect_to_sql_server()
    if app_dal.is_sql_server_connected() is True:
        print("app.py - Sql server is connected")
        if app_dal.connect_to_db() is True:
            print("app.py - Database is connected")
        else:
            print("app.py - Failed to connect to the database, init it")
            if app_dal.init_db() is True:
                print("app.py - Database initialized successfully")
            else:
                print("app.py - Failed to initialize the database")
    else:
        print("app.py - Failed to connect to the sql server")

    if app_dal.connect_to_db() is True:
        # create the item for current instance
        item = EC2DBItem(
                instance_id=EC2MetaData.retrive_instance_id(),
                local_ip=EC2MetaData.retrive_local_ip(),
                public_ip=EC2MetaData.retrive_public_ip(),
                app_port=app_config.server_config.port,
            )
        # create the item for current instance in db
        print("app.py - create or update the item for current instance in db")
        app_dal.create_or_update(item.instance_id, json.dumps(item.to_dict_db()))
        ec2_servers["db_connected"] = True
        ec2_servers["servers"] = []
        # update the db - delete all the items that website is down
        app_dal.update_app_db()
        # read all the items from db
        db_items = app_dal.read_all_items()
        print("app.py - db_items")     
        print(db_items)
        for db_item in db_items:
            item = EC2DBItem(
                instance_id=db_item["instance_info"]["instance_id"], 
                local_ip=db_item["instance_info"]["local_ip"], 
                public_ip=db_item["instance_info"]["public_ip"], 
                app_port=db_item["instance_info"]["app_port"]
            )
            ec2_servers["servers"].append(item.to_dict_view())
    # # else: nothing to do   
    app_dal.close_connection()
    print("app.py - ec2_servers")     
    print(ec2_servers)

    ec2_self = EC2Self()
    data = {
        'is_ec2': ec2_self.is_ec2(),
        'ec2_self': ec2_self.to_list(),
        'static_base_url': app_config.static_config.base_url if app_config.static_config.is_base_url_up() else None,
        'ec2_servers': ec2_servers
    }
    print(data)
    return data


# Route to handle the landing page
@app.route('/', methods=['GET'])
def index():
    print(f"############# app.py - {request.method} method / ##############")
    if request.method == 'GET':
        data = indexData()
        return render_template('index.html', data=data)

    elif request.method == 'HEAD':
        # Handle HEAD request separately
        # Return a minimal response without the response body
        return '', 200
    else:
        # Handle other request methods here
        return '', 405
    
    
# Route to handle the api page
@app.route('/api', methods=['GET', 'HEAD'])
def api():
    print(f"############# app.py - {request.method} method /api ##############")
    if request.method == 'GET':
        data = indexData()
        return jsonify(data)

    elif request.method == 'HEAD':
        # Handle HEAD request separately
        # Return a minimal response without the response body
        return '', 200
    else:
        # Handle other request methods here
        return '', 405


@app.route('/api/configuration', methods=['GET', 'POST', 'HEAD'])
def configuration_route():
    print(f"############# app.py - {request.method} method /api/configuration ##############")
    if request.method == 'POST':

        # get the section, field, value from the json body of request
        section = request.json.get('section', None)
        field = request.json.get('field', None)
        value = request.json.get('value', None)
        found = False

        # the value of section, field, value must be string
        if isinstance(section, str) and isinstance(field, str) and isinstance(value, str):
            if section.lower() == "static":
                if field.lower() == "base_url":
                    app_config.save_configuration_static_base_url(value)
                    found = True
            elif section.lower() == "database":
                if field.lower() == "endpoint":
                    app_config.save_configuration_db_endpoint(value)
                    found = True
                elif field.lower() == "port":
                    app_config.save_configuration_db_port(value)
                    found = True
                elif field.lower() == "user":
                    app_config.save_configuration_db_user(value)
                    found = True
                elif field.lower() == "password":
                    app_config.save_configuration_db_password(value)
                    found = True

        app_config.load_configuration()
        return jsonify(
            {
                "found": found,
                "config": app_config.to_dict()
            })

    elif request.method == 'GET':
        app_config.load_configuration()
        print(app_config.to_dict())
        return jsonify(app_config.to_dict())

    elif request.method == 'HEAD':
        # Handle HEAD request separately
        # Return a minimal response without the response body
        return '', 200
    else:
        # Handle other request methods here
        return '', 405
    # Process the key and value as needed
    # ...
    


@app.route('/loaderio-<string:suffix>/', methods=['GET'])
def loaderio(suffix):
    return f'loaderio-{suffix}', 200

@app.route('/load', methods=['GET'])
def load():
    size = request.args.get('size')  # Get the value of the 'size' query parameter
    if size is None or not size.isdigit() or int(size) <= 0:
        size = '1'  # Set size to 1 if parameter is missing, not an integer, or <= 0
    size_in_kb = int(size)
    # Generate random text content of the specified size
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_kb * 1024))
    response_data = {
        'content': content
    }
    return jsonify(response_data)



if __name__ == '__main__':
    app_init_create_or_update_item()
    # run the http server with port 8080
    app.run(host=app_config.server_config.host, port=app_config.server_config.port)
