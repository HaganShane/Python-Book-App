import BookApp, database
###########################################################
#                                                         #
#  The book's edit a book function                        #
#                                                         #
###########################################################
def editBook():
    connection = database.create_connection()

    if connection is None:
        return
    
    cursor = connection.cursor()

    search_by = input("Enter the field you want to search by (title or ISBN): ").lower()
    if search_by == "title":
        identifier = input("Enter the title of the book you want to modify: ")
        search_query = "SELECT * FROM books WHERE title = %s"
    elif search_by == "isbn":
        identifier = input("Enter the ISBN of the book you want to modify: ")
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

        new_title = input(f"Enter new title (leave blank to keep current, {book[1]}): ") or book[1]
        new_isbn = input(f"Enter new ISBN (leave blank to keep current, {book[2]}): ") or book[2]
        new_author = input(f"Enter new Author (leave blank to keep current, {book[3]}): ") or book[3]
        new_publisher = input(f"Enter new Publisher (leave blank to keep current, {book[4]}): ") or book[4]
        new_date = input(f"Enter new Date (YYYY-MM-DD) (leave blank to keep current, {book[5]}): ") or book[5]
        new_quantity = input(f"Enter new Quantity on hand (leave blank to keep current, {book[6]}): ") or book[6]
        new_wholesale = input(f"Enter new Wholesale Cost (leave blank to keep current, ${book[7]}): ") or book[7]
        new_retail = input(f"Enter new Retail Price (leave blank to keep current, ${book[8]}): ") or book[8]

        update_query = """
        UPDATE books
        SET title = %s, isbn = %s, author = %s, publisher = %s, date_added = %s, qty = %s, wholesale = %s, retail = %s WHERE id = %s
        """

        cursor.execute(update_query, (new_title, new_isbn, new_author, new_publisher, new_date, new_quantity, new_wholesale, new_retail, book[0]))
        connection.commit()

        print("Book updated successfully!")

    else:
        print("Book not found.")
        return
    
    cursor.close()
    connection.close()