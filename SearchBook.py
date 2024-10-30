import BookApp, database
###########################################################
#                                                         #
#  The book look up function                              #
#                                                         #
###########################################################
def lookUpBook():
    connection = database.create_connection()

    if connection is None:
       return []
    
    search_field = input("Enter the field you want to search by (title, ISBN, author, or publisher): ").strip().lower()
    if search_field not in ["title", "ISBN", "author", "publisher"]:
       print("Invalid search field. Please use title, ISBN, author, or publisher.")
       return
    search_value = input("Enter the criteria to search for: ").strip()


    
    search_query = f"SELECT * FROM books WHERE {search_field} = %s"

    cursor = connection.cursor()
    cursor.execute(search_query, (search_value,))

    results = cursor.fetchall()

    if results:
       for row in results:
          print(f"ID: {row[0]}, Title: {row[1]}, ISBN: {row[2]}, Author: {row[3]}, "
                f"Publisher: {row[4]}, Date Added: {row[5]}, Quantity on Hand: {row[6]}, "
                f"Wholesale Price: ${row[7]}, Retail Price: ${row[8]}"
                )
    else:
       print(f"No books found matching that criteria: {search_field} = {search_value}.")

    cursor.close()
    connection.close()

def lookUpAllBooks():
    connection = database.create_connection()
    
    if connection is None:
       return []
    
    cursor = connection.cursor()
    fetch_all_query = "SELECT * FROM books"
    cursor.execute(fetch_all_query)
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    
    if books:
       for book in books:
          print(f"ID: {book[0]}, Title: {book[1]}, ISBN: {book[2]}, Author: {book[3]}, "
                f"Publisher: {book[4]}, Date Added: {book[5]}, Quantity on Hand: {book[6]}, "
                f"Wholesale Price: ${book[7]}, Retail Price: ${book[8]}"
                )
    else:
       print("No books found in database.")
    
    return books