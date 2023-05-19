import configparser


# load configuration from config.ini
def load_configuration():
    config = configparser.ConfigParser()
    config.read('../config.ini')  
    return config