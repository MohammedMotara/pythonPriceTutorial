import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.jdsports.co.uk/product/black-vans-old-skool/1267728/'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

# Can add any price here, depending on what price you'd
# like to purchase the product for

    if(converted_price < 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # server.login('ADD USERNAME', 'ADD PASSWORD')

    subject = 'Price for shoes have fallen down!'
    body = 'Check the Shoe Price - https://www.jdsports.co.uk/product/black-vans-old-skool/1267728/ '

    msg = f"Subject: {subject}\n\n {body}"
    
    server.sendmail(
        'ADD FROM EMAIL',
        'ADD TO EMAIL',
        msg
    )
    #print('Hey EMAIL HAS BEEN SENT')

    server.quit()

''' 

I have addded a sleeper of 24hrs  but this can be adjusted
to suit your needs. The value in the time.sleep() func.
is time in seconds.

'''

while(True)
    check_price()
    time.sleep(86400)

