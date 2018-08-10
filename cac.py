import requests
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

API_KEY="dvt1acaf4bk548fdk8dxkhhb"
#TERM="cactus"


class EtsyClient(object):
    BASE_URL="https://openapi.etsy.com/v2/"

    def search(self,search_term):
        url = self.BASE_URL + "listings/active"
        search_results = self.http_get(url,{"keywords":search_term})
        return search_results

    def item(self,item_id):
    	url = self.BASE_URL + "listings/" + item_id
    	item_results = self.http_get(url)
    	return item_results
    	

    def http_get(self,url,params=None):
    	if params is None:
    		params = {}
    	params["api_key"] = API_KEY
    	resp = requests.get(url, params=params)
    	return resp.json()

		

@app.route("/search/<keyword>")
def search(keyword):
    #resp = requests.get("https://openapi.etsy.com/v2/listings/active", params={"api_key":API_KEY,"keywords":keyword})
    resp = EtsyClient().search(keyword)
    #results = resp.json()["results"]
    results = resp["results"]
    #results = resp.get("results")
    #titles = []
    #or result in results:
    	#titles.append(result["title"])
    # return json.dumps(titles)
    return render_template('search_results.html', results=results)


@app.route("/detail/<item_id>")
def item(item_id):
	#resp = requests.get("https://openapi.etsy.com/v2/listings/" + item_id, params={"api_key":API_KEY})
	resp = EtsyClient().item(item_id)
	results = resp["results"]
	return render_template('detail.html', results=results)

if __name__ == "__main__":
    app.run()
