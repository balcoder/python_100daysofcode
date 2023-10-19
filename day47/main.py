'''Scrape Amazon for product price variations and send email when price of certain
    product fall below set price'''
import smtplib
from email.message import EmailMessage
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')
SEND_TO = os.getenv('SEND_TO')
PRODUCT_URL = "https://www.amazon.co.uk/Logitech-Wireless-Keyboard-Windows-Connection/dp/B00CL6353A/ref=sr_1_3?crid=2LIBBBOD1BADX&keywords=logitech+wireless+keyboard+and+mouse&qid=1697620468&s=computers&sprefix=lo%2Ccomputers%2C86&sr=1-3"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' }

TARGET_PRICE = 21.00
def scrape_amazon(url):
    ''' try get url and scrape using beautiful soup'''
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status() # raise HTTPError, if the response was an http error
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e) from e
    except requests.exceptions.RequestException as e:
        raise SystemExit(e) from e
    if response.status_code == 200:
        wep_page = response.text
        soup = BeautifulSoup(wep_page, 'html.parser')
        a_price = soup.select('span.a-offscreen')
        whole_price =[*a_price[0].getText()]
        whole_price.pop(0)
        price_float = float(''.join(whole_price))
        print(price_float)
        return price_float

    return None

def send_mail(host, user_email, send_to, password, subject, message):
    ''' send email with TLS''' 
    msg = message
    from_ = user_email
    to_ = send_to
    subject = subject
    fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(user=user_email, password=password)
        connection.sendmail(to_, from_, fmt.format(to_, from_, subject, msg).encode('utf-8'))
    print('Email sent')

# email details
my_host = "smtp.gmail.com"
sub = "Amazon Price Target Hit!\n\n"

price =  scrape_amazon(PRODUCT_URL)
if price:    
    if price <= TARGET_PRICE:        
        message_content = f"The product you are watching at {PRODUCT_URL} is below your target £{TARGET_PRICE}"             
        send_mail(host=my_host ,user_email=MY_EMAIL,send_to=SEND_TO, subject=sub, password=MY_PASSWORD, message=message_content)