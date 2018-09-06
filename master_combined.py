import pprint
import json
import requests
import urllib.request

from time import sleep

pp = pprint.PrettyPrinter(depth=50)

g_api_key = "<google api key>"
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

print(f"latitude for {user_address} is {lat} and logitude is {lng}")

print("\nwaiting...\n")
sleep(3)

search_q = input("Please choose a category to search for: ")

y_api_key = '<yahoo api key>'
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': f'Bearer {y_api_key}'}
url_params ={'latitude': lat, 'longitude':
            lng, 'radius': 2500, 'categories': (f'{search_q}, ALL'),
            'sort_by':'distance'}

def func_req(url,url_params, headers):
    response = requests.request('GET', url, headers=headers, params=url_params)
    businesses = response.json()['businesses']
    alias = [business["alias"] for business in businesses]

    print("\nThese 5 places are CLOSE!\n")
    for x in alias[:5]: print(x.replace("-"," "))

func_req(url,url_params,headers)

input('\nPress ENTER to exit')
