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
