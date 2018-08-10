import pprint
import json
import urllib.request

user_key = "<user api key>"

	user_address = input("Please type in your location: ")

def generate_url(address,api_key):
	address = address.replace(" ","+")
	address = address.replace(",","")
	return address 
#string out all non-word characters

result = generate_url(user_address,user_key)

# loc_lookup = f"address={address}&key={api_key}"
# print(loc_lookup)
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?address="
request = f"{endpoint}{result}&key={user_key}"

#just to test...
print(request)

response = urllib.request.urlopen(request).read()
location = json.loads(response)

#pprint.pprint(location['results']['geometry']['location'])

# re-enable after testing?
# latlong_comp = [s['geometry']['location'] for s in location['results']]

# convert to str and sclice out brackets (is this even needed?)
g_user_lat = str([s['geometry']['location']['lat'] for s in location['results']])[1:-1]
g_user_lng = str([s['geometry']['location']['lng'] for s in location['results']])[1:-1]

# convert to float
g_user_lat_float = float(g_user_lat)
g_user_lng_float = float(g_user_lng)
print(f" latitude for {user_address} is {g_user_lat_float} and logitude is {g_user_lng_float}")
