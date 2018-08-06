import urllib.request
import json

# where we are sending our request to
endpoint ="https://maps.googleapis.com/maps/api/directions/json?"

api_key = "<insert your google maps api key here!>"

# get origin
origin = input("Where are you?: ").replace(' ','+')

# get destination
destination = input("Where do you want to go? ").replace(' ','+')

nav_request = f"origin={origin}&destination={destination}&key={api_key}"

request = f"{endpoint}{nav_request}"
response = urllib.request.urlopen(request).read()

directions = json.loads(response)

print(directions)
