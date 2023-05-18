import requests
import configparser
import mysql.connector

# load configuration from config.ini
def loadConfiguration():
    config = configparser.ConfigParser()
    config.read('./config.ini')  
    return config

# Obtain a session token
def obtainSessionToken():
    # Obtain a session token from the metadata service
    TOKEN_URL = 'http://169.254.169.254/latest/api/token'
    TOKEN_TTL = '21600'
    TOKEN_HEADER = {'X-aws-ec2-metadata-token-ttl-seconds': TOKEN_TTL}
    token_response = requests.put(TOKEN_URL, headers=TOKEN_HEADER)
    session_token = token_response.text
    return session_token

# Retrieve the private IP address using the session token
def retrivePrivateIP():
    session_token = obtainSessionToken()
    # Retrieve the private IP address using the session token
    PRIVATE_IP_URL = 'http://169.254.169.254/latest/meta-data/local-ipv4'
    IP_HEADER = {'X-aws-ec2-metadata-token': session_token}
    ip_response = requests.get(PRIVATE_IP_URL, headers=IP_HEADER)
    private_ip = ip_response.text
    return private_ip

# Initialize the database
def initDatabase(endpoint, port, user, password, tableName):
    try:
        connection = mysql.connector.connect(
            host=endpoint,
            port=port,
            user=user,
            password=password,
        )
        cursor = connection.cursor()

        # Check if tableName exists
        cursor.execute(f"SHOW TABLES LIKE '{tableName}'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create the table
            cursor.execute(f"CREATE TABLE {tableName} (id VARCHAR(255), value LONGTEXT)")
            print(f"Table {tableName} created successfully.")
        
        cursor.close()
        connection.close()
        
        return 1
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return 0


# chedk if the webpage is accessible
def checkWebpage(url):
    try:
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
