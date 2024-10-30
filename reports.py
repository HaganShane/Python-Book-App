import helpers, database

def inventory_listing():
    query = "SELECT * FROM books"
    return helpers.execute_query(query, fetch_results=True)

def inventory_wholesale_value():
    query = "SELECT * FROM books ORDER BY wholesale DESC"
    return helpers.execute_query(query, fetch_results=True)

def inventory_retail_value():
    query = "SELECT * FROM books ORDER BY retail DESC"
    return helpers.execute_query(query, fetch_results=True)

def inventory_total_value():
    query = "SELECT title, qty * retail AS total_value FROM books ORDER BY total_value DESC"
    return helpers.execute_query(query, fetch_results=True)

def listing_by_qty():
    query = "SELECT * FROM books ORDER BY qty DESC"
    return helpers.execute_query(query, fetch_results=True)

def greatest_return():
    query = "SELECT *, (wholesale - retail) AS `return` FROM books ORDER BY `return` DESC"
    return helpers.execute_query(query, fetch_results=True)

def listing_by_age():
    query = "SELECT * from books ORDER BY date_added ASC"
    return helpers.execute_query(query, fetch_results=True)

def low_stock():
    query = "SELECT * FROM books WHERE qty <= 5 ORDER BY qty ASC"
    return helpers.execute_query(query, fetch_results=True)

def top_selling():
    query = "SELECT b.title, SUM(s.quantity_purchased) AS total_sold FROM sales s JOIN books b ON s.book_id = b.id GROUP BY b.title ORDER BY total_sold DESC"
    return helpers.execute_query(query, fetch_results=True)

def sales_by_date_range(start_date, end_date):
    query = """
    SELECT b.title, SUM(s.quantity_purchased) AS total_sold, SUM(s.total_price) AS total_revenue FROM sales s
    JOIN books b ON s.book_id = b.id WHERE s.date_purchased BETWEEN %s AND %s GROUP BY b.title
    ORDER BY total_revenue DESC
    """
    return helpers.execute_query(query, (start_date, end_date), fetch_results=True)

def revenue_by_publisher():
    query = """
    SELECT publisher, SUM(total_price) AS total_revenue FROM sales
    JOIN books on sales.book_id = books.id GROUP BY publisher
    ORDER BY total_revenue DESC
    """
    return helpers.execute_query(query, fetch_results=True)

def books_unsold():
    query = "SELECT title FROM books LEFT JOIN sales ON books.id = sales.book_id WHERE sales.book_id IS NULL"
    return helpers.execute_query(query, fetch_results=True)

def out_of_stock():
    query = "SELECT title FROM books WHERE qty = 0"
    return helpers.execute_query(query, fetch_results=True)

def sales_by_author():
    query = """
    SELECT author, SUM(total_price) AS total_revenue FROM sales
    JOIN books ON sales.book_id = books.id GROUP BY author
    ORDER BY total_revenue DESC
    """
    return helpers.execute_query(query, fetch_results=True)

def most_profitable_books():
    query = """
    SELECT title, (retail - wholesale) AS profit_for_book, SUM(quantity_purchased) AS total_profit FROM sales
    JOIN books ON sales.book_id = books.id GROUP BY title ORDER BY total_profit DESC
    """
    return helpers.execute_query(query, fetch_results=True)


def test_reports():
    reports = {
        "Inventory Listing": inventory_listing,
        "Inventory Wholesale Value": inventory_wholesale_value,
        "Inventory Retail Value": inventory_retail_value,
        "Inventory Total Value": inventory_total_value,
        "Listing by Quantity": listing_by_qty,
        "Greatest Return": greatest_return,
        "Listing by Age": listing_by_age,
        "Low Stock Alerts": low_stock,
        "Top Selling Books": top_selling,
        "Sales by Date": lambda: sales_by_date_range('2024-01-01', '2024-08-31')
    }

    for report_name, report_function in reports.items():
        print(f"Testing {report_name}...")
        try:
            rows, headers = report_function()
            if rows:
                helpers.print_table(rows, headers)
            else:
                print("No data returned.")
        except Exception as e:
            print(f"Error occurred while testing {report_name}: {e}")
        print("\n" + "="*50 + "\n")
