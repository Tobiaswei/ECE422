
import MySQLdb as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    """makes a connection to MySQL database.
    @return a mysqldb connection
    """

    #TODO: fill out function parameters. Use the user/password combo for the user you created in 2.1.2.1

    return mdb.connect(host="localhost",
                       user="yuguang2",
                       passwd="password",
                       db="project2");

def createUser(username,password):
    """
    creates a row in table named users
    @param username: username of user
    @param password: password of user
    """
    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query creates a row in table user

    istmt = "INSERT INTO users (username, password, passwordhash) VALUES (%s, %s, %s)"
    m = md5()
    m.update(password)
    cur.execute(istmt, (username, password, m.digest()))

    db_rw.commit()
 
def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()
    ########TODO: Implement aprepared statement using cur.execute() so that this query selects a row from table user
    sel_st=("SELECT * FROM users where username = %(username)s AND password = %(password)s")
    sel_dic={'username':username,'password':password}
    cur.execute(sel_st,sel_dic)
    if cur.rowcount < 1:
        return False
    return True

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """
    fet_st=("SELECT id,username from users where username=%(username)s")
    fet_dic={'username':username}

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    print username
    #TODO: Implement a prepared statement so that this query selects a id and username of the row which has column username = username
    cur.execute(fet_st,fet_dic)
    if cur.rowcount < 1:
        return None
    return FormsDict(cur.fetchone())

def addHistory(user_id, query):
    """ adds a query from user with id=user_id into table named history
    @param user_id: integer id of user
    @param query: the query user has given as input
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statment using cur.execute() so that this query inserts a row in table history
    add_st=("INSERT INTO history(user_id, query) values(%s,%s) ")
    add_tup=(user_id,query)
    cur.execute(add_st,add_tup)
    db_rw.commit()

#grabs last 15 queries made by user with id=user_id from table named history
def getHistory(user_id):
    """ grabs last 15 distinct queries made by user with id=user_id from
    table named history
    @param user_id: integer id of user
    @return a first column of a row which MUST be query
    """

    db_rw = connect()
    cur = db_rw.cursor()
     #TODO: Implement a prepared statement using cur.execute() so that this query selects 15 distinct queries from table history
    add_st=("SELECT query FROM history where user_id = %(user_id)s ORDER BY id DESC LIMIT 15")
    cur.execute(add_st, {'user_id': user_id})
    rows = cur.fetchall();
    return [row[0] for row in rows]
