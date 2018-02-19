from bs4 import BeautifulSoup
import urllib3
import json
import csv
from datetime import datetime




url = 'www.lanacion.com.ar'
url1 = ['https://www.bloomberg.com/quote/SPX:IND','https://www.bloomberg.com/quote/CCMP:IND']


data = []
for page in url1:

 http = urllib3.PoolManager()
 r = http.request('GET',page)

# js =json.loads(r.data.decode('utf-8'))
# print(r.data)
 soup = BeautifulSoup(r.data, 'html.parser')
# print(r.data)
 name_box = soup.find('h1',attrs={'class':'name'}) # h1 because <h1 class="name"> S&amp;P 500 Index </h1> is inside h1
 name = name_box.text
### use soup.select to use  css selectors
# print(soup)
 price_box = soup.find('div',attrs={'class':'price'}) # h1 because <h1 class="name"> S&amp;P 500 Index </h1> is inside h1
 price = price_box.text
### use name = name_box.text.split() where split() will separate name using white space

 ### soup.find is different from soup.find_all, which finds all
 print(name)
 print(price)
 data.append((name,price))

print(data)

# for p in soup.select('p'):
#     if p['id'] =='walrus':
#         print(p.text)

# print(soup.text)
with open('webscraping.csv', 'a') as csv_file: #why 'a'? if use nothing or newline=' ' it gives error
    write = csv.writer(csv_file) # csv_file from above line could be any name
    for name, price in data:
        write.writerow([name,price,datetime.now()])