import requests
import json
from flask import Flask
from flask import render_template
from client import EtsyClient
import MySQLdb 
import os
import database as db


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
    user = client.user(item['user_id'])
    return render_template('detail.html', item=item, user=user)

@app.route("/save-user/<user_id>")
def save_user(user_id):
    client = EtsyClient()
    user = client.user(user_id)
    db.save_user(user)
    # Do Something to save the shop
    return 'OK'

if __name__ == "__main__":
    app.run()
