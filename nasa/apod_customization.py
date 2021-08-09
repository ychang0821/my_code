#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    date = input("Please enter the date(YYYY-MM-DD): ")
    date = "&date=" + date
    ## Call the webservice with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds + date)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))
    if apod.get("media_type") == "image":
        image_url = apod.get("url")
        image_title = apod.get("title")
        urllib.request.urlretrieve(image_url, f"/home/student/static/{image_title}.jpg")
    else:
        print("No image")
    
if __name__ == "__main__":
    main()
