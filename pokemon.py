import requests
from bs4 import BeautifulSoup 
import time 
import lxml

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://google.com",
}

session.headers.update(headers)



bot_token = "8765668348:AAHnmoL5Xecmgv2hN3ewUwsEdpbNh4AUqFA"
chat_id = "8813701657" 
TARGET_URL = "https://www.target.com/p/pokemon-tcg-scarlet-violet-journey-together-8-booster-pack-lot-80-cards/-/A-1003007312#lnk=sametab"




def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message }
    try:
        response = session.post(url, json=payload)
        if response.status_code == 200 :
            print('successfully done by telegram')

        else:
            print(f"telegram failed to send message : {response.text}")
    except Exception as e:
        print(f"something went wrong with telegram : {e}")




while True:
    try:
        print("\nsending requests ....")
        time.sleep(3)
        response = session.get(TARGET_URL , timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            add_to_cart_button = soup.find('button', id='addToCartButtonOrTextIdFor1003007312')
            
            if add_to_cart_button:
                if 'disabled' in add_to_cart_button.attrs:
                    print("the item is not in stock")

                else:
                    
                    alert_msg = f"item is available now in our stock : {TARGET_URL}"
                    send_telegram_alert(alert_msg)
                    break
            else:

                if "Out of stock" not in response.text:
                    alert_msg = f"the product is now available in our website : {TARGET_URL}"
                    send_telegram_alert(alert_msg)
                    break

    except Exception as e:
        print(f"something wrong : {e}")

    print("waiting to send another requests....")
    time.sleep(3)

