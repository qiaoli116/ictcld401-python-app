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
            response = requests.head(self.base_url + "/test.txt")
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

    def load_configuration(self):
        if self.config_file is None:
            raise ValueError("config_file is not set")
        config = configparser.ConfigParser()
        config.read(self.config_file)

        self.server_config.host = config.get('Server', 'host')
        self.server_config.port = config.getint('Server', 'port')

        self.static_config.set_base_url(config.get('Static', 'base_url'))

        self.db_config.endpoint = config.get('Database', 'endpoint')
        self.db_config.port = config.getint('Database', 'port')
        self.db_config.user = config.get('Database', 'user')
        self.db_config.password = config.get('Database', 'password')
        self.db_config.database = config.get('Database', 'database')
        self.db_config.table = config.get('Database', 'table')
