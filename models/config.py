import configparser
import requests
import re

class ServerConfig:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

class StaticConfig:
    def __init__(self, base_url=None):
        # remove trailing slash(s)
        self.set_base_url(base_url)

    def set_base_url(self, base_url):
        if isinstance(base_url, str):
            base_url = re.sub('/+$', '', base_url)
        self.base_url = base_url

    def is_base_url_up(self):
        try:
            response = requests.head(self.base_url + "/test.txt", timeout=1)
            #print (f"reture code {response.status_code}")
            return response.status_code // 100 == 2 or response.status_code // 100 == 3
        except:
            return False



class DBConfig:
    def __init__(self, endpoint=None, port=None, user=None, password=None, database=None, table=None):
        self.endpoint = endpoint
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table

class AppConfig:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.server_config = ServerConfig()
        self.static_config = StaticConfig()
        self.db_config = DBConfig()
        # load configuration
        self.load_configuration()

    def to_dict(self):
        return {
            "server": {
                "host": self.server_config.host,
                "port": self.server_config.port
            },
            "static": {
                "base_url": self.static_config.base_url
            },
            "database": {
                "endpoint": self.db_config.endpoint,
                "port": self.db_config.port,
                "user": self.db_config.user,
                "password": self.db_config.password,
                "database": self.db_config.database,
                "table": self.db_config.table
            }
        } 

    def load_configuration(self):
        if self.config_file is None:
            print("config_file is not set")
        config = configparser.ConfigParser()
        config.read(self.config_file)
        try:

            self.server_config.host = config.get('Server', 'host')
            self.server_config.port = config.getint('Server', 'port')

            self.static_config.set_base_url(config.get('Static', 'base_url'))

            self.db_config.endpoint = config.get('Database', 'endpoint')
            self.db_config.port = config.getint('Database', 'port')
            self.db_config.user = config.get('Database', 'user')
            self.db_config.password = config.get('Database', 'password')
            self.db_config.database = config.get('Database', 'database')
            self.db_config.table = config.get('Database', 'table')
        except:
            print("Error loading configuration file")

    def save_configuration(self, section, field, value):
        if self.config_file is None:
            print("config_file is not set")

        try:
            config = configparser.ConfigParser()
            config.read(self.config_file)
            config.set(section, field, value)
            with open(self.config_file, 'w') as configfile:
                config.write(configfile)
        except Exception:
            print("Error saving configuration file", Exception.args)

    def save_configuration_server_host(self, host):
        self.save_configuration('Server', 'host', host)
    
    def save_configuration_server_port(self, port):
        port_value = -1
        # if port is not integer, try to convert it
        try:
            port_value = int(port)
        except:
            print("Error converting port to integer")
        
        if port_value > 65535 or port_value < 0:
            port_value = 0

        self.save_configuration('Server', 'port', str(port_value))

    def save_configuration_static_base_url(self, base_url):
        self.save_configuration('Static', 'base_url', base_url)

    def save_configuration_db_endpoint(self, endpoint):
        self.save_configuration('Database', 'endpoint', endpoint)

    def save_configuration_db_port(self, port):
        port_value = -1
        # if port is not integer, try to convert it
        try:
            port_value = int(port)
        except:
            print("Error converting port to integer")
        
        if port_value > 65535 or port_value < 0:
            port_value = 0
        
        self.save_configuration('Database', 'port', str(port_value))
    
    def save_configuration_db_user(self, user):
        self.save_configuration('Database', 'user', user)

    def save_configuration_db_password(self, password):
        self.save_configuration('Database', 'password', password)

    @staticmethod
    def reset_configuration(source_config_file, target_config_file):
        # copy source_config_file to target_config_file
        try:
            with open(source_config_file, 'r') as source:
                with open(target_config_file, 'w') as target:
                    target.write(source.read())
        except Exception:
            print("Error resetting configuration file", Exception.args)
        

    
