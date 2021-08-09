#!/usr/bin/python3

import requests
import time
import reverse_geocoder
  
URL= "http://api.open-notify.org/iss-now.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()
    lon = resp.get("iss_position")["longitude"]
    lat = resp.get("iss_position")["latitude"]
    ts = resp["timestamp"]

    # string from time
    ts = time.strftime("%Y-%m-&d %H:%M:%S", time.gmtime(ts))
    
    city = reverse_geocoder.search((lat, lon))[0]["name"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    City: {city}
    """)
main()




