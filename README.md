# Google-Maps-API-Project
An application that has you choose your location, and various statistics are pulled up that correlate with your chosen location.

Here is how it should work:

The program asks the user to input their location.  A specific address, or a generic city name should work.
The prgram asks the user what they want to look for.

Say you gave the address for Pioneer Square in Portland, OR, and type "bar" for the type of business you want to find.  The application will spit out the 5 closest business that match that business type to the provided address.

I really want this application to have more functionality in the future, but for right now, I want to get the basics ironed out.

Written using Python 3.7.  This code uses "f strings", which are not currently compatble with Python 2.7 at the time of writing this comment.  F strings are compatible with Python 3.6 and up.

The file that needs love right now is master_combined.py

TO-DO:
- ~~pull lat and long based off of location~~
- ~~access other apis to generate values based off of lat and long~~
- ~~use lat and long from google to query yelp~~
- return MEANINGFUL results
- test google places api to see if it can potentially replace using google maps + yelp

Partially Complete / Needs Love
- allow the user to select what they are looking for (bar, restaurant, food cart, etc)


Long-Term stuff:
- create a web application (flask/docker?) that makes this aplpication more user-friendly
- incorperate the ability to drop a pin on your desired location in an embedded google map
