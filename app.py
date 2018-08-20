import requests
import json
from flask import Flask
from flask import render_template
from client import EtsyClient
import MySQLdb 


app = Flask(__name__)

search_term = 'cacti'
		
@app.route("/")
def index():
    return search(search_term)

@app.route("/search/<keyword>")
def search(keyword):
    resp = EtsyClient().search(keyword)
    results = resp["results"]
    return render_template('search_results.html', results=results)


@app.route("/detail/<item_id>")
def item(item_id):
    client = EtsyClient()
    item = client.item(item_id)
    shop = client.shop(item['user_id'])
    return render_template('detail.html', item=item, shop=shop)


MYSQL_HOST= os.getenv('MYSQL_HOST')
MYSQL_USER= os.getenv('MYSQL_USER')
MYSQL_PASSWORD= os.getenv('MYSQL_PASSWORD')
DATABASE_NAME= os.getenv('DATABASE_NAME')

def connectDB():
    db = MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,DATABASE_NAME)
    return db


if __name__ == "__main__":
    app.run()
