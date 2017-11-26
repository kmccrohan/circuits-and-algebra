import mysql.connector
import tabulate
import config

# global DB connection
con = None

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
    print tabulate.tabulate(rows, headers=trim_attrs(attributes))
    rs.close()

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