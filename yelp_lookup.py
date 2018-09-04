  
import pprint
import requests
import json
 
pp = pprint.PrettyPrinter(depth=6)

API_key = '<insert API key here!>'
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': f'Bearer {API_key}'}

# now sorting properly by passing in a tuple as a value for the 'categories' key
url_params ={'latitude': 45.518792, 'longitude':
            -122.678864, 'radius': 500, 'categories': ('bars, ALL'),
            'sort_by':'distance'}

def func_req(url,url_params, headers):
    response = requests.request('GET', url, headers=headers, params=url_params)
    fin_response = response.json()
    pp.pprint(fin_response)

func_req(url,url_params,headers)
