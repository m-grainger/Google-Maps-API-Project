  
import pprint
import requests
import json
 
pp = pprint.PrettyPrinter(depth=6)

API_key = '<yelp api key>'
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': f'Bearer {API_key}'}
url_params ={'latitude': 45.518147, 'longitude':
            -122.679602, 'radius': 500, 'term': 'tavern'}

def func_req(url,url_params, headers):
    response = requests.request('GET', url, headers=headers, params=url_params)
    fin_response = response.json()
    pp.pprint(fin_response)

func_req(url,url_params,headers)
