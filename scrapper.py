import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-28-70mm-Accessory/dp/B07KMWQBMY/ref=sr_1_1_sspa?crid=3S6QTMO7NOBD7&dchild=1&keywords=sony+a7iii&qid=1612550774&sprefix=sony+%2Caps%2C189&sr=8-1-spons&psc=1&smid=AXCB29L39I26U&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzN1NTOVZGWEMzWUdJJmVuY3J5cHRlZElkPUEwNTI4MDA0M1ZIRTQzNFdKMU1VTSZlbmNyeXB0ZWRBZElkPUEwNzQwNTI2M01VTEdXQU5ROExYWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="productTitle").get_text()   # this finds the product title Span within the URL given
    price = soup.find(id="priceblock_saleprice").get_text() # this finds the product price as priceblock_saleprice
    converted_price = float(price[0:5])  # extract just the first five characters in the price and wraps it in a float


    if(converted_price < 1.999):
        send_mail()



    print(converted_price)

    print(title.strip())  # strips out alll of the data minus the white space

    if(converted_price < 1.999):
        send_mail



def send_mail():
    server = smtplib.STMP('stmp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('FROM EMAIL LOGIN HERE', 'FROM EMAIL PASSWORD HERE') #login with user and PW. Defined in secrets

    subject = 'Sony A7 Price lowered!'
    body = 'Check the Amazon link! https://www.amazon.com/Sony-Mirrorless-Digital-28-70mm-Accessory/dp/B07KMWQBMY/ref=sr_1_1_sspa?crid=3S6QTMO7NOBD7&dchild=1&keywords=sony+a7iii&qid=1612550774&sprefix=sony+%2Caps%2C189&sr=8-1-spons&psc=1&smid=AXCB29L39I26U&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzN1NTOVZGWEMzWUdJJmVuY3J5cHRlZElkPUEwNTI4MDA0M1ZIRTQzNFdKMU1VTSZlbmNyeXB0ZWRBZElkPUEwNzQwNTI2M01VTEdXQU5ROExYWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject} \n\n{body}"   # formatting message
    #send message, from, to , message
    server.sendmail(
        'YOUR FROM HERE'
        'YOUR TO HERE'
        msg
    )
    print('E-mail Successfully Sent')

    server.quit()


    while(True):
        check_price()
        time.sleep(86400)  # this pauses the running of the application by 60 seconds.  Adjust the sleep time, in seconds to your liking


