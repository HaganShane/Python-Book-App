import tkinter
import tkinter.messagebox

import tkinter.test
import helpers, reports

def open_cashier():
    tkinter.messagebox.showinfo("Cashier Module", "Cashier Module Loaded")

def open_inventory():
    inventory_window = tkinter.Toplevel(root)
    inventory_window.title("Inventory Database")

    add_button = tkinter.Button(inventory_window, text="Add Book", command=add_book)
    add_button.pack(pady=5)

    edit_button = tkinter.Button(inventory_window, text="Edit Book", command=edit_book)
    edit_button.pack(pady=5)

    delete_button = tkinter.Button(inventory_window, text="Delete Book", command=delete_book)
    delete_button.pack(pady=5)
    

def open_reports():
    reports_window = tkinter.Toplevel(root)
    reports_window.title("Reporting")
    report_buttons = [
        ("Inventory Listing", reports.inventory_listing),
        ("Wholesale Value", reports.inventory_wholesale_value),
        ("Retail Value", reports.inventory_retail_value),
        ("Total Value", reports.inventory_total_value),
        ("Quantity Listing", reports.listing_by_qty),
        ("Greatest Return", reports.greatest_return),
        ("Listing by Age", reports.listing_by_age),
        ("Low Stock", reports.low_stock),
        ("Top Selling", reports.top_selling),
        ("Sales By Date Range", reports.sales_by_date_range),
        ("Revenue By Publisher", reports.revenue_by_publisher),
        ("Books Unsold", reports.books_unsold),
        ("Out of Stock", reports.out_of_stock),
        ("Sales by Author", reports.sales_by_author),
        ("Most Profitable Books", reports.most_profitable_books),
    ]

    for report_name, report_func in report_buttons:
        button = tkinter.Button(reports_window, text=report_name, command=lambda f=report_func: show_report(f))
        button.pack(pady=5)

def add_book():
    tkinter.messagebox.showinfo("Add Book", "Add Book Module Loaded")
    
def edit_book():
    tkinter.messagebox.showinfo("Edit Book", "Edit Book Module Loaded")

def delete_book():
    tkinter.messagebox.showinfo("Delete Book", "Delete Book Module Loaded")

def show_report(report_func):
    report_window = tkinter.Toplevel(root)
    report_window.title("Reports")
    rows, header = report_func()

    result_text = "\n".join([" | ".join(map(str, row)) for row in rows])

    text_area = tkinter.Text(report_window)
    text_area.insert(tkinter.END, result_text)
    text_area.pack()

def on_quit():
    root.destroy()

root = tkinter.Tk()
root.title("Book Inventory System")

cashier_button = tkinter.Button(root, text="Cashier Module", command=open_cashier)
cashier_button.pack(pady=10)

inventory_button =  tkinter.Button(root, text="Inventory Module", command=open_inventory)
inventory_button.pack(pady=10)

report_button =  tkinter.Button(root, text="Report Module", command=open_reports)
report_button.pack(pady=10)

quit_button = tkinter.Button(root, text="Quit", command=on_quit)
quit_button.pack(pady=10)

root.mainloop()