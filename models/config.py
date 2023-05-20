import configparser

class ServerConfig:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

class StaticConfig:
    def __init__(self, base_url=None):
        self.base_url = base_url

class DBConfig:
    def __init__(self, endpoint=None, port=None, user=None, password=None):
        self.endpoint = endpoint
        self.port = port
        self.user = user
        self.password = password

class AppConfig:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.server_config = ServerConfig()
        self.static_config = StaticConfig()
        self.db_config = DBConfig()
        self.load_configuration()

    def load_configuration(self):
        if self.config_file is None:
            raise ValueError("config_file is not set")
        config = configparser.ConfigParser()
        config.read(self.config_file)

        self.server_config.host = config.get('Server', 'host')
        self.server_config.port = config.getint('Server', 'port')

        self.static_config.base_url = config.get('Static', 'base_url')

        self.db_config.endpoint = config.get('Database', 'endpoint')
        self.db_config.port = config.getint('Database', 'port')
        self.db_config.user = config.get('Database', 'user')
        self.db_config.password = config.get('Database', 'password')
