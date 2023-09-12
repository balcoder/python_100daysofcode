''' Check stock for increase/decrease in price for last two days
    and if over 5% send sms message to phone using twilio with
    first 3 news articles on stock for previous day '''

from datetime import datetime, timedelta
import requests
from twilio.rest import Client
from api_key import NEWS_API_KEY, ALPHA_VANTAGE_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_news(stock) -> list:
    ''' gets the first 3 news articles from yestersay to now'''
    yesterday_datetime = datetime.now() - timedelta(1)
    yesterday = datetime.strftime(yesterday_datetime, '%Y-%m-%d')
    news_params = {
        "q": stock,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params, timeout=10)
    response.raise_for_status()
    data = response.json()
    first_3 = data['articles'][:3]
    return first_3


def get_stock_price(stock_name) -> float:
    ''' given stock name return % up or down from last 2 days trading '''
    stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": ALPHA_VANTAGE_KEY
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params, timeout=10)
    response.raise_for_status()
    data = response.json()
    first_2 = list(data["Time Series (Daily)"].items())[:2]   
    close_price1 = float(first_2[0][1]['4. close'])
    close_price2 = float(first_2[1][1]['4. close'])
    price_diff = abs(close_price1 - close_price2)
    price_avg = (close_price1 + close_price2) / 2    
    percentage_diff = round(((price_diff / price_avg) * 100), 2)
    if close_price1 - close_price2 < 0:
        return -percentage_diff
    else:
        return percentage_diff

def send_sms(message):
    ''' use twilio to send sms text message '''
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+15627413568',
        body=message,
        to='+353866067654'
        )
    print(message.status)

stock_price_deviation = get_stock_price(STOCK)
if stock_price_deviation > 5.0:
    movement = "🔺"
elif stock_price_deviation < -5.0:
    movement = "🔻"
if stock_price_deviation > 5.0 or stock_price_deviation < -5.0:
    three_articles = get_news(COMPANY_NAME)
    for article in three_articles:
        # print(f"Article: {article}\n")
        message = (
            f"{STOCK} {movement} {stock_price_deviation}\nHeadline:"
            f"{article['title']}\n{article['description']}\n"
            f"URL: {article['url']}"
            )
        send_sms(message)
print(get_stock_price(STOCK))
