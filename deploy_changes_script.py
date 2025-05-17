import mysql.connector

# Database connection details
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "Secret5555"
DB_NAME = "test_db"

# SQL command to create a table if it doesn't already exist
sql_change = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    
    # Execute the SQL command to make changes
    cursor.execute(sql_change)
    
    # Save (commit) the changes to the database
    conn.commit()
    print("Database changes deployed successfully.")
    
except mysql.connector.Error as err:
    # Print any error that occurs during the process
    print(f"Error: {err}")

finally:
    # Close cursor and connection to free resources
    if conn.is_connected():
        cursor.close()
        conn.close()
