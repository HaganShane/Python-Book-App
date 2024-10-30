####################################
#                                  #
# CMPSC 122 Project Baseline       #
#                                  #
####################################
import datetime
import operator
import time
import AddBook, cashier, DeleteBook, EditBook, SearchBook, reports

###########################################################
# bookData will consist of the following information      #
#  title:     The book title                              #
#  isbn:      The ISBN number of a book                   #
#  author:    The author’s name                           #
#  publisher: The publisher’s name                        #
#  date:      The date the book was added to inventory    #
#  qty:       The quantity on hand of the book            #
#  wholesale: The wholesale cost of the book              #
#  retail:    The retail price of the book                #
###########################################################

############################
# Create a list named bookData.
#   Initialize the list to an empty list
#############################
bookData = []

###########################################################
#                                                         #
#  The bookInfo function displays the Book Information    #
#  Screen                                                 #
#                                                         #
###########################################################
def bookInfo(bookData):
    print("\t\t\tSerendipity Booksellers\n")
    print("\t\t\t    Book Information\n\n")
    print("Title: " + bookData[0])
    print("ISBN: " + bookData[1])
    print("Author: " + bookData[2])
    print("Publisher: " + bookData[3])
    print("Date Added: " + bookData[4])
    print("Quantity-On-Hand: " + str(bookData[5]))
    print("Wholesale Cost: %.2f" % float(bookData[6]))
    print("Retail Price: %.2f" % float(bookData[7]))
    print("\n\n")


# ********************************************************
# The invMenu function displays the Inventory Database   *
# Menu                                                   *
# ********************************************************
def invMenu():
    choice = 0	# To hold the user's choice

    # Display the menu until the user selects item 5
    while choice != 6:
        print( "Serendipity Booksellers\n")
        print( "  Inventory Database\n\n")

        print( "1.Look Up all Book\n")
        print( "2.Look up specific Book\n")
        print( "3.Add a Book\n")
        print( "4.Edit a Book's Record\n")
        print( "5.Delete a Book\n")
        print( "6.Return to the Main Menu\n\n")

        # Get the choice as input from the user
        choice = int(input( "Enter Your Choice: "))
        
        # Validate the user's input
        while choice < 1 or choice > 6:
            print( "\nPlease enter a number in the range 1 - 6.\n")
            choice = int(print( "Enter Your Choice: "))
                
        # Display the selection
        if choice == 1:
            SearchBook.lookUpAllBooks()
        elif choice == 2:
            SearchBook.lookUpBook()
        elif choice == 3:
            AddBook.addBook()
        elif choice == 4:
            EditBook.editBook()
        elif choice == 5:
            DeleteBook.deleteBook()
        elif choice == 6:
            print( "\nYou left the Inventory Menu.\n")

# ********************************************************
# The reports function displays the Reports Menu         *
# ********************************************************
def report():
    reports.test_reports()


#######################################
#   Main Program
#######################################
choice = 0	# To hold the user's menu choice

# Display the menu until the user selects item 4
while choice != 4:
    print( "Serendipity Booksellers\n")
    print( "\tMain Menu\n\n")

    print( "1.Cashier Module\n")
    print( "2.Inventory Database Module\n")
    print( "3.Report Module\n")
    print( "4.Exit\n\n")

    # Get the menu choice as input from the user
    choice = int(input("Enter Your Choice: "))
    
    # Validate the user's input
    while choice < 1 or choice > 4:
        print( "\nPlease enter a number in the range 1 - 4.\n")
        choice = int(input( "Enter Your Choice: "))
            
    # Display the selection
    if choice == 1:
        cashier.cashier()
    elif choice == 2:
        invMenu()
    elif choice == 3:
        report()
    else:
        print("Leaving the Book Inventory Program")