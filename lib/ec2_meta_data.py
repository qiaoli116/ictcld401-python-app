import mysql.connector
import requests

# Obtain a session token
def obtain_session_token():
    # Obtain a session token from the metadata service
    TOKEN_URL = 'http://169.254.169.254/latest/api/token'
    TOKEN_TTL = '21600'
    TOKEN_HEADER = {'X-aws-ec2-metadata-token-ttl-seconds': TOKEN_TTL}
    token_response = requests.put(TOKEN_URL, headers=TOKEN_HEADER)
    session_token = token_response.text
    return session_token

def retrieve_meta_data(item):
    # Define meta items
    meta_items = {
        "local-ipv4", 
        "public-ipv4",
        "instance-id"
    }
    if item not in meta_items:
        return None

    session_token = obtain_session_token()
    # Build the URL to retrieve the meta data
    ITEM_URL = 'http://169.254.169.254/latest/meta-data/' + item
    # Add the session token to the header
    HEADER = {'X-aws-ec2-metadata-token': session_token}

    try:
        # Retrieve the meta data
        response = requests.get(ITEM_URL, headers=HEADER)
        # Raise an exception for non-2xx status codes
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle the exception or log the error
        print(f"Error occurred: {e}")
        return None


# Retrieve the private IP address using the session token
def BACKUP_retrive_private_ip():
    session_token = obtain_session_token()
    # Retrieve the private IP address using the session token
    PRIVATE_IP_URL = 'http://169.254.169.254/latest/meta-data/local-ipv4'
    IP_HEADER = {'X-aws-ec2-metadata-token': session_token}
    ip_response = requests.get(PRIVATE_IP_URL, headers=IP_HEADER)
    private_ip = ip_response.text
    return private_ip

# Retrieve the local IP address using the session token
def retrive_local_ip():
    return retrieve_meta_data("local-ipv4")

# Retrieve the local IP address using the session token
def retrive_instance_id():
    return retrieve_meta_data("instance-id")

# Retrieve the local IP address using the session token
def retrive_public_ip():
    return retrieve_meta_data("public-ipv4")