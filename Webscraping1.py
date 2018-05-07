#this is a script to pull info from imdb for movies based on a specific query

import json
import urllib3
from bs4 import BeautifulSoup


url = 'www.google.com'

http = urllib3.PoolManager()
r = http.request('Get',url)
print(r.data)

# js =json.loads(r.data.decode('utf-8'))
