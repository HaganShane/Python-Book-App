import mysql.connector 
from mysql.connector import errorcode

DB_NAME = "book_inventory"
TABLES = {
    'books': (
        "CREATE TABLE IF NOT EXISTS `books` ("
        " `id` INT AUTO_INCREMENT PRIMARY KEY,"
        " `title` VARCHAR(255) NOT NULL,"
        " `isbn` VARCHAR(20) UNIQUE NOT NULL,"
        " `author` VARCHAR(255) NOT NULL,"
        " `publisher` VARCHAR(255) NOT NULL,"
        " `date_added` DATE NOT NULL,"
        " `qty` INT DEFAULT 0,"
        " `wholesale` DECIMAL(10,2) NOT NULL,"
        " `retail` DECIMAL(10,2) NOT NULL"
        ") ENGINE=InnoDB"),

    'sales': (
        " CREATE TABLE IF NOT EXISTS `sales` ("
        " `sale_id` INT AUTO_INCREMENT PRIMARY KEY,"
        " `book_id` INT NOT NULL,"
        " `date_purchased` DATE NOT NULL,"
        " `quantity_purchased` INT NOT NULL,"
        " `total_price` DECIMAL(10,2) NOT NULL,"
        " FOREIGN KEY (book_id) REFERENCES books(id)"
        ") ENGINE=InnoDB")
}

def create_connection():
    try:
        connection = mysql.connector.connect(
            user = "root",
            password = "password",
            host = "localhost",
            database = "book_inventory"
        )
        return connection
    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None
    
def create_db(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database, {DB_NAME}, created successfully.")
    except mysql.connector.Error as error:
        print(f"Failed to create database, with error: {error}")
        exit(1)

def create_table(cursor):
    for table_name, table_description in TABLES.items():
        try:
            cursor.execute(f"USE {DB_NAME}")
            cursor.execute(table_description)
            print(f"Table, '{table_name}', created successfully.")
        except mysql.connector.Error as error:
            print(f"Failed creating table, '{table_name}', with error: {error}")

def initialize_db():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        create_db(cursor)
        create_table(cursor)
        cursor.close()
        connection.close()

initialize_db()