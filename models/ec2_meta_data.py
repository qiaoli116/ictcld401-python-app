import mysql.connector
import requests

class EC2MetaData:
    # Obtain a session token
    def obtain_session_token():
        try:
            # Obtain a session token from the metadata service
            TOKEN_URL = 'http://169.254.169.254/latest/api/token'
            TOKEN_TTL = '21600'
            TOKEN_HEADER = {'X-aws-ec2-metadata-token-ttl-seconds': TOKEN_TTL}
            token_response = requests.put(TOKEN_URL, headers=TOKEN_HEADER, timeout=1)
            session_token = token_response.text
            return session_token
        except requests.exceptions.RequestException as e:
            # Handle the exception or log the error
            print(f"obtain_session_token Error occurred: {e}")
            return None

    def retrieve_meta_data(item):
        # Define meta items
        meta_items = {
            "local-ipv4", 
            "public-ipv4",
            "instance-id"
        }
        if item not in meta_items:
            return None

        session_token = EC2MetaData.obtain_session_token()
        if session_token is None:
            return None

        # Build the URL to retrieve the meta data
        ITEM_URL = 'http://169.254.169.254/latest/meta-data/' + item
        # Add the session token to the header
        HEADER = {'X-aws-ec2-metadata-token': session_token}

        try:
            # Retrieve the meta data
            response = requests.get(ITEM_URL, headers=HEADER, timeout=0.5)
            # Raise an exception for non-2xx status codes
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            # Handle the exception or log the error
            print(f"retrieve_meta_data({item}) Error occurred: {e}")
            return None

    # Retrieve the local IP address using the session token
    def retrive_local_ip():
        return EC2MetaData.retrieve_meta_data("local-ipv4")

    # Retrieve the local IP address using the session token
    def retrive_instance_id():
        return EC2MetaData.retrieve_meta_data("instance-id")

    # Retrieve the local IP address using the session token
    def retrive_public_ip():
        return EC2MetaData.retrieve_meta_data("public-ipv4")