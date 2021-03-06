import mysql.connector
import tabulate
import config

# global DB connection
con = None

# --------------------------- INSERT ----------------------------------
# Adds a copy to the database
def add_copy(book_id, library_id):
    insert = "INSERT INTO `copy` (`library_id`, `book_id`) VALUES ('%s', '%s')" % (library_id, book_id)
    rs = con.cursor()
    rs.execute(insert)
    con.commit()

# Adds a book to the database. Returns the book_id of the newly created book.
def add_book(title, author):
    insert = "INSERT INTO `book` (`title`, `author`) VALUES ('%s', '%s')" % (title, author)
    rs = con.cursor()
    rs.execute(insert)
    con.commit()
    return rs.lastrowid

# Adds a checkout to the database. Returns the book_id of the newly created book.
def checkout_copy(librarian_id, copy_id, member_id, checkout_date):
    insert = "INSERT INTO `checkout` VALUES ('%s', '%s', '%s', '%s', NULL)" % (librarian_id, copy_id, member_id, checkout_date)
    rs = con.cursor()
    rs.execute(insert)
    con.commit()

# Adds a member to the database
def add_member(member_name, address, phone):
    insert = "INSERT INTO `member` (`member_name`, `address`, `phone`) VALUES ('%s', '%s', '%s')" % (member_name, address, phone)
    rs = con.cursor()
    rs.execute(insert)
    con.commit()

# --------------------------- UPDATE ----------------------------------
# Updates the checkin date to be not null.
def checkin_copy(copy_id, date):
    update = "UPDATE checkout SET checkin_date='%s' WHERE copy_id=%d AND checkin_date IS NULL" % (date, copy_id)
    rs = con.cursor()
    rs.execute(update)
    con.commit()

# -------------------------- DELETE ------------------------------------
# Deletes the specified copy.
def delete_copy(copy_id):
    delete = "DELETE FROM `copy` WHERE copy_id=%d" % copy_id
    rs = con.cursor()
    rs.execute(delete)
    con.commit()

# -------------------------- SELECT ------------------------------------

# Returns number of results. Prints if more than 0 results. Same params as query.
def print_query(*args, **kwargs):
    rows = query(*args, **kwargs)
    if len(rows) > 0:
        print_results(rows, args[0])
    return len(rows)

def print_results(rows, attrs):
    print tabulate.tabulate(rows, headers=trim_attrs(attrs))

# Returns rows of results. Does not print results.
def query(attributes, _from, where=None, orderby=None, groupby=None, having=None, limit=None):
    rs = con.cursor()
    attrString = ','.join(attributes)
    query = 'SELECT ' + attrString + ' from ' + _from
    if where is not None:
        query += ' where ' + where
    if orderby is not None:
        query += ' order by ' + orderby
    if groupby is not None:
        query += ' group by ' + groupby
    if having is not None:
        query += ' having ' + having
    if limit is not None:
        query += ' limit ' + str(limit)
    rs.execute(query)
    rows = []
    for row in rs:
        rows.append(row)
    rs.close()
    return rows

def trim_attrs(attributes):
    t_attrs = []
    for att in attributes:
        if '.' in att:
            t_attrs.append(att.split(".",1)[1])
        else:
            t_attrs.append(att)
    return t_attrs

# -- DB connections ---------------

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
        dab = config.mysql['database']
        # create a connection
        con = mysql.connector.connect(user=usr,password=pwd, host=hst,
                                      database=dab)

    except mysql.connector.Error as err:
        print err
