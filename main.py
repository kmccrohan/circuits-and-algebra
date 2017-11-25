import tabulate
import query

librarian_id = None

# -------------------------- Utils --------------------------------

# ----------------------------- Queries ---------------------------

def testCopyAtLocation():
    print "not done"

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
    print "1. check out a copy"
    print "2. check in a copy"
    print "3. Add a copy of book"
    print "4. Remove a copy"
    print "5. Register a new library member"
    print "6. Query information"
    print "7. Exit"
    return input("Enter your choice (1-7): ")

# Main control of flow of program. Loops until user exits
def control():
    choice = displayMenu()
    print "-------------------------"
    if choice == 1:
        checkoutCopy()
    elif choice == 2:
        checkinCopy()
    elif choice == 3:
        addCopy()
    elif choice == 4:
        removeCopy()
    elif choice == 5:
        registerMember()
    elif choice == 6:
        queryControl()
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
    print "Below are the available librarian options:"
    query.query(['librarian_id', 'librarian_name'], 'librarian')
    librarian_id = input("Please enter your librarian id: ")

def main():
    query.connect()
    login()
    control()

if __name__ == '__main__':
    main()
