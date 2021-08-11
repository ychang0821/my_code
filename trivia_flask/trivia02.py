#!usr/bin/python3

import requests

# the URL you wish to post to
url = 'http://192.168.0.66:2224/check'

# the data you wish to post
dict = {'an': 'soccer'}

x = requests.post(url, data = dict)

print (x.text)