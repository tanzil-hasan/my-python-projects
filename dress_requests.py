import requests 
from bs4 import BeautifulSoup
import time
import lxml
import os 

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

all_html_content = session.get('https://www.vibrantbd.com/')
#print(all_html_content.text)

mother_soup = BeautifulSoup(all_html_content.text, 'lxml')
#print(mother_soup.prettify())

view_all = mother_soup.select("header.section__header>a")
#print(view_all)


main_links = []

for each_part in view_all:

    main_link = each_part.get('href')

    if 'https://www.vibrantbd.com' not in main_link :

        custom_link = 'https://www.vibrantbd.com'+main_link
        main_links.append(custom_link)

    else :
        main_links.append(main_link)

#print(main_links)
#print(len(main_links))

product_catagory = 'ladies-fashion,shirts,mens-sandal,men-casual-shoe,best-selling'.split(',')
#print(a)

print('UPLOADING CATAGORY FROM WEBPAGE....')
time.sleep(1.3)

options = """
1 . LADIES FASHION 👜👠👗💅🏻💄

2 . SHIRTS 👔👕👚

3 . MENS SANDAL 🩴

4 . MEN CASUAL SHOE 👞👟🥾

5 . BEST SELLING ✨🎉🎗️🎈✨
"""
print(options)

while True : 
    user_input = input ('PLEASE ENTER THE INDEX ONLY >>>> ').strip()

    if user_input in ['1','2','3','4','5'] :
        idx = int(user_input)-1
        break

    else : 
        print('\t\t ENTER A VALID INDEX ONLY \n')

file_name = product_catagory[idx]


with open(f'{file_name}.txt' , 'a'  , encoding='UTF-8') as f :

    html_for_specific_main_link = session.get(main_links[idx])
    child_soup = BeautifulSoup(html_for_specific_main_link.text, 'lxml')

    product_links = child_soup.select('div.product-item__info-inner > a')

    print(f'\n{len(product_links)} PRODUCTS FOUNDED\n')
    
    try :
        for every_product_link in product_links :

            every_product_href = every_product_link.get('href')

            if 'https://www.vibrantbd.com' not in every_product_href :

                every_product_href = 'https://www.vibrantbd.com'+every_product_href
                html_for_every_product = session.get(every_product_href)
                
            else :
                html_for_every_product = session.get(every_product_href)
                

            product_soup = BeautifulSoup(html_for_every_product.text, 'lxml')
        
            name = product_soup.select_one('h1.product-meta__title').text
            sku = product_soup.select_one('span.product-meta__sku-number').text
            price = product_soup.select_one('span.price').text

            design = '='*50
            datas = f'\nNAME : {name.strip()}\nSKU : {sku.strip()}\nPRICE : {price.strip()}\n\n{design}\n\n'

            file_submit = f.writelines(datas)
            print('collecting...')
            time.sleep(1.5)
            print('PRODUCT-DATA COLLECTED SUCCESSFULLY \n ')
            

    except Exception  as e : 
        print(f' Product not found \n {e}')

print('Done'.center(50,'-'))