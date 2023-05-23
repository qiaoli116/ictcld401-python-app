import mysql.connector
import requests
import json

class AppDAL:
    def __init__(self, host, port, user, password, database, table):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.conn = None
        self.cursor = None

    def connect_to_sql_server(self):
        try:
            self.conn = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=None # do not connec to the database yet
            )
            print(f"Connected to the sql server: {self.host}:{self.port}")
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to the sql server: {e}")

    def is_sql_server_connected(self):
        return self.conn is not None and self.cursor is not None

    def connect_to_db(self):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return False

        try:
            self.cursor.execute(f"USE {self.database}")
            print(f"Connected to the database: {self.database}")
            return True
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {self.database} {e}")
        return False

    def init_db(self):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return False

        # create the database if doe not exist
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Database {self.database} created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating database: {e}")
            return False
        # connect to the database
        if self.connect_to_db():
            # create the table if does not exist
            try:
                self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (instance_id VARCHAR(255) PRIMARY KEY, instance_info JSON)")
                print(f"Table {self.table} created successfully.")
                return True
            except mysql.connector.Error as e:
                print(f"Error creating table: {e}")
        return False


    def create_item(self, instance_id, instance_info):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return

        try:
            sql = f"INSERT INTO {self.table} (instance_id, instance_info) VALUES (%s, %s)"
            values = (instance_id, instance_info)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating item: {e}")

    def read_all_items(self):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return None

        try:
            self.cursor.execute(f"SELECT instance_id, instance_info FROM {self.table}")
            items = self.cursor.fetchall()
            print(f"rowcount: {len(items)}")
            result = []
            for item in items:
                result.append({
                    "instance_id": item[0],
                    "instance_info": json.loads(item[1])}
                    )
            return result
        except mysql.connector.Error as e:
            print(f"Error reading items: {e}")
        return None

    def read_one_item(self, instance_id):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return None

        try:
            print(f"instance_id: {instance_id}")
            sql = f"SELECT * FROM {self.table} WHERE instance_id = %s"
            values = (instance_id,)
            self.cursor.execute(sql, values)
            item = self.cursor.fetchone()
            print(f"item: {item}")
            return item
        except mysql.connector.Error as e:
            print(f"Error reading item: {e}")
        return None

    def update_item(self, instance_id, new_instance_info):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return

        try:
            sql = f"UPDATE {self.table} SET instance_info = %s WHERE instance_id = %s"
            values = (new_instance_info, instance_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error updating item: {e}")

    def delete_item(self, instance_id):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return
            
        try:
            sql = f"DELETE FROM {self.table} WHERE instance_id = %s"
            values = (instance_id,)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error deleting item: {e}")

    def close_connection(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.conn is not None:
                self.conn.close()
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")

    # a function to retrive public ip of all instances from database
    def retrieve_all_public_ip (self):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return None

        try:
            sql = f"SELECT instance_id, JSON_UNQUOTE(JSON_EXTRACT(instance_info, '$.public_ip')) as public_ip FROM {self.table}"
            self.cursor.execute(sql)
            items = self.cursor.fetchall()
            print(f"items: {items}")
            result = []
            for item in items:
                result.append({
                    "instance_id": item[0],
                    "public_ip": item[1]}
                    )
            return result
        except:
            print(f"something wrong with the sql query or result")
        return None

    # a function to retrive public ip based on the instance id from database
    def retrieve_public_ip (self, instance_id):
        # check if self.conn is None or self.cursor is None
        if self.is_sql_server_connected() is False:
            print("Sql server is not connected. Please connect to the sql server first.")
            return

        try:
            print(f"instance_id: {instance_id}")
            sql = f"SELECT JSON_UNQUOTE(JSON_EXTRACT(instance_info, '$.public_ip')) as public_ip FROM {self.table} WHERE instance_id = %s"
            values = (instance_id,) # must inlcude the "," to create a tuple with one element
            self.cursor.execute(sql, values)
            item = self.cursor.fetchone()
            print(f"item: {item}")
            value = item[0]
            return value
        except:
            print(f"something wrong with the sql query or result")
        return None

    # a function retrive public ip first and then verify if http://public_ip:app_port is up
    def is_website_public_ip_up(self, instance_id, public_ip, app_port):
        #public_ip = self.retrieve_public_ip(instance_id)
        print(f"is_website_public_ip_up - instance_id: {instance_id}, public ip: {public_ip}, app_port: {app_port}")
        if public_ip is None:
            return False
        else:
            try:
                print(f"is_website_public_ip_up - try to connect to http://{public_ip}:{app_port}")
                response = requests.head(f"http://{public_ip}:{app_port}", timeout=1)
                status_code = response.status_code
                print (f"Website is up reture code {status_code}", flush=True)
                return status_code // 100 == 2 or status_code // 100 == 3
            except:
                print("Error connecting to the website.")
        return False

    # loop all instances and verify if http://public_ip:app_port is up
    # if not up, delete the instance from database
    # use the function retrieve_all_public_ip, is_website_public_ip_up, delete_item
    def update_app_db(self):
        items = self.retrieve_all_public_ip()
        print(f"update_app_db - Total items: {len(items)}")
        print(f"update_app_db - items: {items}")
        x = items[5]
        items[5] = items[3]
        items[3] = x
        print(f"update_app_db - items again: {items}")
        for item in items:
            print(f"update_app_db - {item}")
            is_website_up = self.is_website_public_ip_up(item["instance_id"], item["public_ip"], 8080)
            print(f"update_app_db - is_website_up: {is_website_up}")
            if not is_website_up:
                print(f"update_app_db - instance {item['instance_id']} is not up, delete it from database")
            #     self.delete_item(item["instance_id"])
            else:
                print(f"update_app_db - instance {item['instance_id']} is up, keep it in database")
       
