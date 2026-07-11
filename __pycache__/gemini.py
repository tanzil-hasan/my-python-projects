import requests 
from bs4 import BeautifulSoup
import time
import lxml
import os 

# স্ক্রিন ক্লিয়ার করা
os.system('cls' if os.name == 'nt' else 'clear')

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://google.com",
}
session.headers.update(headers)

# হোমপেজ থেকে মেইন লিংকগুলো নেওয়া
print("Loading categories from website...")
all_html_content = session.get('https://www.vibrantbd.com/')
mother_soup = BeautifulSoup(all_html_content.text, 'lxml')

view_all = mother_soup.select("header.section__header > a")
main_links = []

for each_part in view_all:
    main_link = each_part.get('href', '')
    if 'https://www.vibrantbd.com' not in main_link:
        custom_link = 'https://www.vibrantbd.com' + main_link
        main_links.append(custom_link)
    else:
        main_links.append(main_link)

# ক্যাটাগরি এবং অপশন সেটআপ
categories_filenames = ['ladies-fashion', 'shirts', 'mens-sandal', 'men-casual-shoe', 'best-selling']

options = """
1 . LADIES FASHION 
2 . SHIRTS
3 . MENS SANDAL
4 . MEN CASUAL SHOE
5 . BEST SELLING
"""
print(options)

# ইউজার ইনপুট ভ্যালিডেশন (সঠিক ইনপুট না দেওয়া পর্যন্ত লুপ চলবে)
while True:
    user_input = input("Please enter the index only (1-5) >>>> ").strip()
    if user_input in ['1', '2', '3', '4', '5']:
        idx = int(user_input) - 1 # লিস্ট ইনডেক্স ০ থেকে শুরু হয়
        break
    else:
        print('INVALID INPUT! PLEASE TRY AGAIN...')

# নির্বাচিত ক্যাটাগরির কাজ শুরু
selected_link = main_links[idx]
filename = f'{categories_filenames[idx]}.txt'

print(f"\nFetching products from: {selected_link}")
inside_main_link = session.get(selected_link)
child_soup = BeautifulSoup(inside_main_link.text, 'lxml')

# প্রোডাক্টের লিংকগুলো খুঁজে বের করা
all_product_link = child_soup.select('div.product-item__info-inner > a')
print(f"Found {len(all_product_link)} products. Starting download...\n")

with open(filename, 'a', encoding='UTF-8') as f:
    for each_link in all_product_link:
        href = each_link.get('href')
        if not href.startswith('http'):
            href = 'https://www.vibrantbd.com' + href
            
        try:
            product_infos = session.get(href)
            product_soup = BeautifulSoup(product_infos.text, 'lxml')

            # সেফলি ডেটা এক্সট্রাক্ট করা (যাতে কোনোটা মিসিং থাকলে কোড বন্ধ না হয়)
            name_el = product_soup.select_one('h1.product-meta__title')
            sku_el = product_soup.select_one('span.product-meta__sku-number')
            price_el = product_soup.select_one('.price, span.product-meta__price') # মাল্টিপল চয়েস সিলেক্টর

            name = name_el.text.strip() if name_el else "N/A"
            sku = sku_el.text.strip() if sku_el else "N/A"
            price = price_el.text.strip() if price_el else "N/A"

            # ফরম্যাট করে ফাইলে রাইট করা
            end = '='*50    
            datas = f'NAME : {name}\nSKU : {sku}\nPRICE : {price}\n{end}\n'
            f.write(datas) # writelines এর বদলে write ব্যবহার করা ভালো একক স্ট্রিং এর জন্য
            print(f"Saved: {name} - {price}")
            
            # অ্যান্টি-বট মেজারমেন্ট (সার্ভারে চাপ না দিতে)
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Error scraping product {href}: {e}")

print(f"\nDone! All data saved to {filename}")
#Compose
