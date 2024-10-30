import BookApp, database, datetime
# ********************************************************
# The cashier function displays the Cashier Module       *
# ********************************************************
def cashier():
    SALES_TAX_RATE = 0.06	# The sales tax


    print( "Serendipity Booksellers\n")
    print( " Cashier Module\n\n")

    connection = database.create_connection()

    if connection is None:
        return
    
    cursor = connection.cursor()

    search_by = input("Enter the field you want to search by (title or ISBN): ").lower()
    if search_by == "title":
        identifier = input("Enter the title of the book you want to purchase: ")
        search_query = "SELECT * FROM books WHERE title = %s"
    elif search_by == "isbn":
        identifier = input("Enter the ISBN of the book you want to purchase: ")
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

        purchase_qty = int(input("Enter the quantity of books you intend to purchase: "))

        if purchase_qty > book[6]:
            print("Not enough stock available. Please try a lower quantity.")
            return
        
        subtotal = float(book[8] * purchase_qty)
        sales_tax = SALES_TAX_RATE * subtotal
        total = subtotal + sales_tax

        print("\n---------- Receipt ----------")
        print(f"Title: {book[1]}")
        print(f"ISBN: {book[2]}")
        print(f"Quantity: {purchase_qty}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}\n")

        confirm_purchase = input(f"Would you like to purchase {purchase_qty} copy(ies) of {book[1]} for a total of ${total:.2f}? (enter y/yes or n/no): ").strip().lower()
        if confirm_purchase not in ['y', 'yes']:
            print("Purchased cancelled. Have a good day.")
            return
        
        updated_qty = book[6] - purchase_qty
        update_qty_query = "UPDATE books SET qty = %s WHERE id = %s"
        cursor.execute(update_qty_query, (updated_qty, book[0]))

        insert_sale_query = "INSERT INTO sales (book_id, date_purchased, quantity_purchased, total_price) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_sale_query, (book[0], datetime.date.today(), purchase_qty, total))
        connection.commit()

        print(f"Purchase complete! You bought {purchase_qty} copy(ies) of {book[1]} for a total of ${total:.2f}. Thank you for shopping with us and have a wonderful day!")

        cursor.close()
        connection.close()

    else:
        print("Book not found in our inventory. Have a manager use the add a book module if you think this is a mistake.")
        return

