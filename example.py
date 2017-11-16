import mysql.connector
import config

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

# Lists out countries in database
def listCountries():
    rs = con.cursor()
    query = 'SELECT country_name, code from country'
    rs.execute(query)
    print "Countries:"
    for (name, code) in rs:
        print name + " (" + code + ")"

    rs.close()

# Returns true if country code already exists in database.
def countryExists(code):
    rs = con.cursor()
    query = "SELECT COUNT(*) from country where code = '%s'" % (code)
    rs.execute(query)
    count = rs.fetchone()[0]
    rs.close()
    return int(count) > 0

# Inserts the country and its attributes into the database
def insertCountry(values):
    insert = "INSERT INTO country VALUES ('%s', '%s', %d, %d)" % values
    rs = con.cursor()
    rs.execute(insert)
    con.commit()

# Adds a country to the database
def addCountry():
    code = raw_input("Country Code: ")
    name = raw_input("Country Name: ")
    gdp = input("Country GDP (usd): ")
    inflation = float(raw_input("Country Inflation (pct): "))
    if not countryExists(code):
        insertCountry((code, name, gdp, inflation))
        print "Added country"
    else:
        print "Country code already exists!"

# Selects countries that meet the specified parameters.
def selectCountries(values):
    rs = con.cursor()
    query = ("SELECT country_name, code, gdp, inflation from country "
            "WHERE gdp >= %d AND inflation <= %d "
            "ORDER BY gdp DESC, inflation ASC "
            "LIMIT %d" % values)
    rs.execute(query)
    print "Countries that meet specifications:"
    for data in rs:
        print "%s (%s), %s, %s" % data
    rs.close()

# Find country based on gdp and inflation.
def findCountries():
    n = input("Number of countries to display: ")
    minGdp = input("Min GDP (usd): ")
    maxInflation = float(raw_input("Max Inflation (pct): "))
    selectCountries((minGdp, maxInflation, n))

# Updates the database with country's gdp and inflation
def updateValues(values):
    update = "UPDATE country Set gdp = %d, inflation = %d WHERE code = '%s'" % values
    rs = con.cursor()
    rs.execute(update)
    con.commit()

# Update gdp and inflation of a country
def updateCountry():
    code = raw_input("Country Code: ")
    gdp = input("Country GDP (usd): ")
    inflation = float(raw_input("Country Inflation (pct): "))
    if not countryExists(code):
        print "Country does not exist!"
    else:
        updateValues((gdp, inflation, code))
        print "Updated country"

# Main control of flow of program. Loops until user exits
def control():
    choice = displayMenu()
    print "-------------------------"
    if choice == 1:
        listCountries()
    elif choice == 2:
        addCountry()
    elif choice == 3:
        findCountries()
    elif choice == 4:
        updateCountry()
    elif choice == 5:
        print "Bye..."
        disconnect()
        quit()
    else:
        print "Invalid choice!"

    control()

def main():
    connect()
    control()

if __name__ == '__main__':
    main()
