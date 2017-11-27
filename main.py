import tabulate
import query

librarian_id = None

# -------------------------- Utils --------------------------------
# Helper function for selecting a library ID
def selectLibrary():
    query.print_query(['library_id', 'library_name'], 'library')
    return input("Please enter the library id: ")

# Helper function for selecting a book ID
def selectBook():
    # query.query(['book_id', 'title', 'author'], 'book')
    # return input("Please enter the book id: ")
    while True:
        title = raw_input("What is your book title? ")
        print "Is one of these books?"
        if (query.print_query(['book_id', 'title', 'author'], 'book',
                        where="title LIKE '%" + title + "%' ")):
            return input("Please enter your book id: ")
        else:
            print "No matching books. Try again."

# Helper function for selecting a member ID
def selectMember():
    query.print_query(['member_id', 'member_name'], 'member')
    return input("Please enter the member id: ")

# Helper function for selecting an author
def selectAuthor():
    while True:
        author = raw_input("What is the name of the author? ")
        print "Is it one of these authors?"
        if (query.print_query(['author'], 'book',
                        where="author LIKE '%" + author + "%' ")):
            return raw_input("Please type the author name exactly as it appears above: ")
        else:
            print "No matching authors. Try again."

# ----------------------------- Queries ---------------------------

# Checks to see if a copy of a book is available at a specific library
def testCopyAtLocation():
    library_id = selectLibrary()
    book_id = selectBook()
    results = query.query(['book_id'], 'copy',
                        where=('book_id=%d AND library_id=%d' % (book_id, library_id)))
   
    # only display the list if the list isn't empty; otherwise, return an error
    if len(results) > 0:
        print "There are %d copies of this book at this location." % len(results)
    else:
        print "No copies of this book at this location."

# Displays the number of books checked out by a specific member
def booksCheckedOutByMember():
    member_id = selectMember()
    results = query.query(['member_id'], 'checkout',
                        where=('member_id=%d AND checkin_date IS NULL' % member_id))
    print "This member currently has %d books checked out." % len(results)

# Displays the libraries where copies of a specific book are available
def availableCopiesOfBook():
    book_id = selectBook()
    results = query.query(['library_name'],'book JOIN copy USING (book_id) JOIN checkout USING (copy_id) JOIN library USING (library_id)',
			where=('book_id = %d AND checkin_date IS NOT NULL' % book_id))

    # only display the list if the list isn't empty; otherwise, return an error
    if len(results) > 0:
       print "There are %d copies of this book available. \nThey can be found at the following locations: " % len(results)
       query.print_results(results, ['library_name'])
    else:
        print "No copies of this book are currently available."

# Displays the titles of books by a specific author
def booksByAuthor():
    author = selectAuthor()
    results = query.query(['title'],'book',
		where=('author = "%s" ' % author))

    # only display the list if the list isn't empty; otherwise, return an error
    if len(results) > 0:
	print "\nHere are all of the books by %s :" % author
        query.print_results(results, ['title'])
    else:
	print "No books by this author are in the system."

# Returns the author who has the most number of books in the system
def mostProlificAuthor():
    print "not done"

# Returns the customer who has the most number of books checked out on their account
def mostProlificCustomer():
    print "not done"

# Returns the number of books at a specific library
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
    print "7. How many copies of books per library"
    print "8. Cancel"
    return input("Enter your choice (1-8): ")

# Menu for Query Selection
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

# Allows the user to check out a copy of a book to a member
def checkoutCopy():
    print "not done"

# Allows the user to check in a copy of a book
def checkinCopy():
    print "not done"

# First creates book if book is not defined
def addCopy():
    print "not done"

# Removes a copy of a book from the database
def removeCopy():
    print "not done"

# Enters a new member into the database
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