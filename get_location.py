import json
import urllib.request

user_key = "<insert your google maps api key here!>"
	
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

print(location)
