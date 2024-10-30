import BookApp, database
###########################################################
#                                                         #
#  The book's delete a book function                      #
#                                                         #
###########################################################
def deleteBook():
    connection = database.create_connection()

    if connection is None:
        return
    
    cursor = connection.cursor()

    search_by = input("Enter the field you want to search by (title or ISBN): ").lower()
    if search_by == "title":
        identifier = input("Enter the title of the book you want to delete: ")
        search_query = "SELECT * FROM books WHERE title = %s"
    elif search_by == "isbn":
        identifier = input("Enter the ISBN of the book you want to delete: ")
        search_query = "SELECT * FROM books WHERE isbn = %s"
    else:
        print("Invalid entry. Please enter title or ISBN.")
        return
    
    cursor.execute(search_query, (identifier,))
    book = cursor.fetchone()

    if book:
        print("Current book information: ")
        print(f"Title: {book[1]}")
        print(f"ISBN: {book[2]}")
        print(f"Author: {book[3]}")
        print(f"Publisher: {book[4]}")
        print(f"Date Added: {book[5]}")
        print(f"Quantity On Hand: {book[6]}")
        print(f"Wholesale Cost: ${book[7]}")
        print(f"Retail Price: ${book[8]}")

        confirmation = input("\nAre you sure you would like to delete this book? (enter y/yes or n/no): ").strip().lower()

        if confirmation in ('y', 'yes'):
            delete_query = "DELETE FROM books WHERE id = %s"
            cursor.execute(delete_query, (book[0],))
            connection.commit()
            print("Book has been deleted successfully.")
        else:
            print("Book deletion has been cancelled. Book still exists in inventory.")
    else:
        print("Book not found, please try again")
    
    cursor.close()
    connection.close()