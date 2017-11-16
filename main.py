import mysql.connector
import config
import tabulate

# global DB connection
con = None

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
        dab = 'kmccrohan_DB'
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst,
                                      database=dab)

    except mysql.connector.Error as err:
        print err

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
        print "Bye..."
        disconnect()
        quit()
    else:
        print "Invalid choice!"

    control()

# Returns the integer menu choice
def displayMenu():
    print "----------------------------------"
    print "Choose from the following options:"
    print "1. List countries"
    print "2. Add country"
    print "3. Find countries based on gdp and inflation"
    print "4. Update country's gdp and inflation"
    print "5. Exit"
    return input("Enter your choice (1-5): ")

def main():
    connect()
    control()

if __name__ == '__main__':
    main()
