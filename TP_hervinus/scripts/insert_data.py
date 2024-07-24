import mysql.connector
from config.db_config import DB_CONFIG

def insert_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    insert_query = """
    INSERT INTO ma_table (Height,width, target) 
    VALUES (%s, %s, %s)
    """
    
    data = [
        (1.0, 2.0, 3.0),
        (2.0, 4.0, 6.0),
        (3.0, 6.0, 9.0),
    ]
    
    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_data()
