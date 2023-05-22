import mysql.connector

class AppDAL:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user='your_username',
                password='your_password',
                host='your_host',
                port='your_port_number',
                database='python-app'
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

    def is_db_server_up(self):
        try:
            self.conn.ping(reconnect=True)
            return True
        except mysql.connector.Error:
            return False

    def is_db_created(self):
        try:
            self.cursor.execute("SELECT 1 FROM servers LIMIT 1")
            return True
        except mysql.connector.Error:
            return False

    def init_db(self):
        try:
            self.cursor.execute("USE python-app")
        except mysql.connector.Error as e:
            if e.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                try:
                    self.cursor.execute("CREATE DATABASE python-app")
                    self.cursor.execute("USE python-app")
                except mysql.connector.Error as e:
                    print(f"Error creating database: {e}")
                    return

        try:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS servers ("
                "instance_id VARCHAR(255) PRIMARY KEY,"
                "instance_info JSON"
                ")"
            )
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")

    def create_item(self, instance_id, instance_info):
        try:
            sql = "INSERT INTO servers (instance_id, instance_info) VALUES (%s, %s)"
            values = (instance_id, instance_info)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating item: {e}")

    def read_all_items(self):
        try:
            self.cursor.execute("SELECT * FROM servers")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error reading items: {e}")

    def read_one_item(self, instance_id):
        try:
            sql = "SELECT * FROM servers WHERE instance_id = %s"
            values = (instance_id,)
            self.cursor.execute(sql, values)
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Error reading item: {e}")

    def update_item(self, instance_id, new_instance_info):
        try:
            sql = "UPDATE servers SET instance_info = %s WHERE instance_id = %s"
            values = (new_instance_info, instance_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error updating item: {e}")

    def delete_item(self, instance_id):
        try:
            sql = "DELETE FROM servers WHERE instance_id = %s"
            values = (instance_id,)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error deleting item: {e}")

    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")



if __name__ == '__main__':
# Create an instance of AppDAL
app_dal = AppDAL()

# Check if the MySQL database server is up
if app_dal.is_db_server_up():
    # Check if the "servers" table exists
    if app_dal.is_db_created():
        # Create a new item
        instance_id = "12345"
        instance_info = '{"name": "Server 1", "status": "active"}'
        app_dal.create_item(instance_id, instance_info)
        print("Item created successfully.")
    else:
        print("The 'servers' table does not exist.")
        # Initialize the database and create the 'servers' table
        app_dal.init_db()
else:
    print("Could not connect to the MySQL database server.")

# Close the database connection
app_dal.close_connection()