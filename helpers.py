import database
from mysql.connector import Error

def execute_query(query, params=None, fetch_results=False):
    connection = database.create_connection()
    
    if connection is None:
        return None
    cursor = connection.cursor()
    try:
        
        cursor.execute(query, params)
        if fetch_results:
            result = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            cursor.close()
            return result, column_names
        
        else:
            connection.commit()
    except Error as error:
        print(f"Error: {error}")

    finally:
        cursor.close()
        connection.close()


def print_table(rows, column_names):
    print(" | ".join(column_names))
    print("-" * (len(column_names) * 20))
    for row in rows:
        print(" | ".join(map(str, row)))