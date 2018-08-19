import requests
import json
from config import *
from flask import Flask
from flask import render_template
from client import EtsyClient


app = Flask(__name__)

		
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
	resp = EtsyClient().item(item_id)
	results = resp["results"]
	return render_template('detail.html', results=results)

if __name__ == "__main__":
    app.run()
