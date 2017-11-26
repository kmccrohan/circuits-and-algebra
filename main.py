import tabulate
import query

librarian_id = None

# -------------------------- Utils --------------------------------
def selectLibrary():
    query.print_query(['library_id', 'library_name'], 'library')
    return input("Please enter the library id: ")

def selectBook():
    # query.query(['book_id', 'title', 'author'], 'book')
    # return input("Please enter the book id: ")
    while True:
        title = raw_input("What is your book title? ")
        print "Is one of these the book?"
        if (query.print_query(['book_id', 'title', 'author'], 'book',
                        where="title LIKE '%" + title + "%' ")):
            return input("Please enter your book id: ")
        else:
            print "No matching books. Try again."

# ----------------------------- Queries ---------------------------

def testCopyAtLocation():
    library_id = selectLibrary()
    book_id = selectBook()
    results = query.query(['book_id', 'library_id'], 'copy',
                        where=('book_id=%d AND library_id=%d' % (book_id, library_id)))
    if len(results) > 0:
        print "There are %d copies of this book at this location." % len(results)
    else:
        print "No copies of this book at this location."

def booksCheckedOutByMember():
    print "not done"

def availableCopiesOfBook():
    print "not done"

def booksByAuthor():
    print "not done"

def mostProlificAuthor():
    print "not done"

def mostProlificCustomer():
    print "not done"

def copiesPerLibrary():
    print "not done"

# Returns the integer menu choice
def displayQueryMenu():
    print "----------------------------------"
    print "Please select from one of the following query options:"
    print "1. See if there is a copy of a book at a specific location"
    print "2. How many books a member currently has checked out"
    print "3. Find available copies of a specific book"
    print "4. Find books by a specific author"
    print "5. Find authors that has most books in system"
    print "6. Return customer who has checked out the most books overall"
    print "7. How many copis of books per library"
    print "8. Cancel"
    return input("Enter your choice (1-8): ")

def queryControl():
    choice = displayQueryMenu()
    print "-------------------------"
    if choice == 1:
        testCopyAtLocation()
    elif choice == 2:
        booksCheckedOutByMember()
    elif choice == 3:
        availableCopiesOfBook()
    elif choice == 4:
        booksByAuthor()
    elif choice == 5:
        mostProlificAuthor()
    elif choice == 6:
        mostProlificCustomer()
    elif choice == 7:
        copiesPerLibrary()
    elif choice == 8:
        control()
    else:
        print "Invalid choice!"
    queryControl()

# --------------------------- Actions -------------------------------

def checkoutCopy():
    print "not done"

def checkinCopy():
    print "not done"

# First creates book if book is not defined
def addCopy():
    print "not done"

def removeCopy():
    print "not done"

def registerMember():
    print "not done"

# Returns the integer menu choice
def displayMenu():
    print "----------------------------------"
    print "Choose from the following options:"
    print "1. Query information"
    print "2. check out a copy"
    print "3. check in a copy"
    print "4. Add a copy of book"
    print "5. Remove a copy"
    print "6. Register a new library member"
    print "7. Exit"
    return input("Enter your choice (1-7): ")

# Main control of flow of program. Loops until user exits
def control():
    choice = displayMenu()
    print "-------------------------"
    if choice == 1:
        queryControl()
    elif choice == 2:
        checkoutCopy()
    elif choice == 3:
        checkinCopy()
    elif choice == 4:
        addCopy()
    elif choice == 5:
        removeCopy()
    elif choice == 6:
        registerMember()
    elif choice == 7:
        print "Bye..."
        query.disconnect()
        quit()
    else:
        print "Invalid choice!"

    control()

# asks user for librarian id
def login():
    global librarian_id
    print "Welcome to the library system!"
    query.print_query(['librarian_id', 'librarian_name'], 'librarian')
    librarian_id = input("Please enter your librarian id: ")

def main():
    query.connect()
    login()
    control()

if __name__ == '__main__':
    main()
