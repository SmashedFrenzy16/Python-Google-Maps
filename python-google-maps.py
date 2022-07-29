from pygeocoder import Geocoder

import time


placeName = input("Enter a place name: ")

time.sleep(0.5)

print("Searching Google Maps for {}".format(placeName))

time.sleep(1)

results = Geocoder.geocode(placeName)

for result in results:
  
  print(result)
