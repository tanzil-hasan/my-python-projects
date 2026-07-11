import requests 
from bs4 import BeautifulSoup as beautifulsoup
import os 
import time
import lxml


os.system('cls')
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
 "Referer": "https://google.com",
}

session.headers.update(headers)
data = session.get("https://zuqo.shop/collections/mens-sandal")
#print(data.text)

soup = beautifulsoup(data.text , 'lxml')
#print(soup.prettify())

 #  /products/zuqo-heritage-sandal-strap
a_links =[]
h2 = soup.find_all('h2' , class_ = 'product-card-title fw-500' )
#print(h2)

for part in h2 : 
    link = part.a['href']
    a_links.append(link)

#print(a_links)
with open('shoes.txt' , 'a' , encoding='UTF-8')  as f : 
    for every_link in a_links:
        info = session.get("https://zuqo.shop"+every_link)
        time.sleep(4)
        #print(info.text)

        new_soup = beautifulsoup(info.text, 'lxml')

        product_titles = new_soup.find_all('h2' , class_ = 'h1')
        all_prices= new_soup.find_all('span' , class_ = 'price-item price-item--regular')
        stocks = new_soup.find_all('p' , class_= 'product__inventory no-js-hidden')

        for title, price, stock in zip(product_titles,all_prices,stocks) :

            design = '*'*50
            details = (f'''{title.text.strip()}\n{price.text.strip()}\n{stock.text.strip()}\n{design}\n\n''')

            ap = f.writelines(details)
print('done')





