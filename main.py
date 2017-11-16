import mysql.connector
import config
import tabulate

# global DB connection
con = None
librarian_id = None

def disconnect():
    global con
    con.close()

def connect():
    global con
    try:
        # connection info
        usr = config.mysql['user']
        pwd = config.mysql['password']
        hst = config.mysql['host']
        dab = 'library_project'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst,
                                      database=dab)

    except mysql.connector.Error as err:
        print err

# ----------------------------- Queries ---------------------------
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
    print "7. How many books per library"
    print "8. Cancel"
    return input("Enter your choice (1-8): ")

def queryControl():
    choice = displayQueryMenu()
    print "-------------------------"
    if choice == 1:
        print "not done"
    elif choice == 2:
        print "not done"
    elif choice == 3:
        print "not done"
    elif choice == 4:
        print "not done"
    elif choice == 5:
        print "not done"
    elif choice == 6:
        print "not done"
    elif choice == 7:
        print "not done"
    elif choice == 8:
        control()
    else:
        print "Invalid choice!"
    queryControl()

# --------------------------- Actions -------------------------------
# Returns the integer menu choice
def displayMenu():
    print "----------------------------------"
    print "Choose from the following options:"
    print "1. check out a copy"
    print "2. check in a copy"
    print "3. Add a book or copy of book"
    print "4. Remove a copy or book"
    print "5. Register a new library member"
    print "6. Query information"
    print "7. Exit"
    return input("Enter your choice (1-7): ")

# Main control of flow of program. Loops until user exits
def control():
    choice = displayMenu()
    print "-------------------------"
    if choice == 1:
        print "not done"
    elif choice == 2:
        print "not done"
    elif choice == 3:
        print "not done"
    elif choice == 4:
        print "not done"
    elif choice == 5:
        print "not done"
    elif choice == 6:
        queryControl()
    elif choice == 7:
        print "Bye..."
        disconnect()
        quit()
    else:
        print "Invalid choice!"

    control()

# asks user for librarian id
def login():
    global librarian_id
    print "Welcome to the library system!"
    librarian_id = input("Please enter your librarian id: ")

def main():
    connect()
    login()
    control()

if __name__ == '__main__':
    main()
