
# Initialize the database
def init_database(endpoint, port, user, password, tableName):
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
        return None

