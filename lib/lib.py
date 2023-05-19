import requests
import configparser


# load configuration from config.ini
def load_configuration():
    config = configparser.ConfigParser()
    config.read('./config.ini')  
    return config

# chedk if the webpage is accessible
def is_webpage_up(url):
    try:
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
