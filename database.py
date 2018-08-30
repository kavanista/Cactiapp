import MySQLdb 
import os

MYSQL_HOST= os.getenv('MYSQL_HOST')
MYSQL_USER= os.getenv('MYSQL_USER')
MYSQL_PASSWORD= os.getenv('MYSQL_PASSWORD')
DATABASE_NAME= os.getenv('DATABASE_NAME')

def connectDB():
    db = MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,DATABASE_NAME)
    return db

def get_all(db=None):
    if not db:
        db = connectDB()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = """ SELECT * FROM users  """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def save_user(user,db=None):
    if not db:
        db = connectDB()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = " INSERT into users VALUES (0,%(uid)s, %(first_name)s, %(sold_count)s, %(img)s )"
    data = {
        "uid": user['user_id'],
        "first_name": user['first_name'],
        "sold_count": user['transaction_sold_count'],
        "img": user['image_url_75x75']
    }
    try:
        cursor.execute(query,data)
        db.commit() 
    except ValueError as error:
    	print data,query
