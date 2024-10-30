import BookApp, database
import mysql.connector
###########################################################
#                                                         #
#  The book's add a new book function                     #
#                                                         #
###########################################################
def addBook():
    connection = database.create_connection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("USE book_inventory")
        title = input("Enter book title: ")
        isbn = input("Enter ISBN: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        date_added = input("Enter date (YYYY-MM-DD): ")
        qty = int(input("Enter quantity: "))
        wholesale = float(input("Enter wholesale price: "))
        retail = float(input("Enter retail price: "))

        add_book_query = (
            "INSERT INTO books (title, isbn, author, publisher, date_added, qty, wholesale, retail) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )

        data = (title, isbn, author, publisher, date_added, qty, wholesale, retail)
        cursor.execute(add_book_query, data)
        connection.commit()

        print("Book has been added successfully.")
        cursor.close()
        connection.close()
