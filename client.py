import requests


API_KEY = 'oru4yxzoc36x15p4krgn5opo'


class EtsyClient(object):

    BASE_URL="https://openapi.etsy.com/v2/"

    def search(self, search_term):
        url = self.BASE_URL + "listings/active"
        search_results = self.http_get(url, {"keywords": search_term})
        return search_results

    def item(self, item_id):
    	url = self.BASE_URL + "listings/" + item_id
    	item_results = self.http_get(url)
    	return item_results	

    def shop(self, shop_id):
        url = self.BASE_URL + 'shops/{}'.format(shop_id)
        return self.http_get(url)

    def shop_listings(self, shop_id):
        url = self.BASE_URL + 'shops/{}/listings/active'.format(shop_id)
        return self.http_get(url)
    
    def http_get(self, url, params=None):
    	if params is None:
    		params = {}
    	params["api_key"] = API_KEY
    	resp = requests.get(url, params=params)
    	return resp.json()
