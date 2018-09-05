import pprint
import json
import requests
import urllib.request

from time import sleep

pp = pprint.PrettyPrinter(depth=6)

# api credentials
g_api_key = "<google maps api key>"
y_api_key = '<yelp api key>'

user_address = input("Please type in your location: ")

def generate_url(address,api_key):
	address = address.replace(" ","+")
	address = address.replace(",","")
	return address 
#string out all non-word characters

result = generate_url(user_address,g_api_key)

endpoint = "https://maps.googleapis.com/maps/api/geocode/json?address="
request = f"{endpoint}{result}&key={g_api_key}"

g_response = urllib.request.urlopen(request).read()
location = json.loads(g_response)

# fix this... encountering bugs with converting to float, and it looks sloppy.
# sometimes it doesn't want to convert to floats. adding a print statement magically makes this work.

g_user_lat = str([s['geometry']['location']['lat'] for s in location['results']]).replace('[','').replace(']','')
print()
g_user_lat = float(g_user_lat)
lat = g_user_lat

g_user_lng = str([s['geometry']['location']['lng'] for s in location['results']]).replace('[','').replace(']','')
print()
g_user_lng = float(g_user_lng)
lng = g_user_lng

print(f" latitude for {user_address} is {lat} and logitude is {lng}")

print("waiting...")
sleep(5)


url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': f'Bearer {y_api_key}'}
url_params ={'latitude': lat, 'longitude':
            lng, 'radius': 500, 'categories': ('bars, ALL'),
            'sort_by':'distance'}

def func_req(url,url_params, headers):
    response = requests.request('GET', url, headers=headers, params=url_params)
    fin_response = response.json()
    pp.pprint(fin_response)

func_req(url,url_params,headers)

input('Press ENTER to exit')
