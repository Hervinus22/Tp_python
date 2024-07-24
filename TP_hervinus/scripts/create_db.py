import mysql.connector
from config.db_config import DB_CONFIG

def create_database_and_table():
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS Regression_db")
    cursor.execute("USE Regression_db")
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS DataRegression (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Height FLOAT,
        Width FLOAT,
        target FLOAT
    )
    """
    cursor.execute(create_table_query)
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database_and_table()
