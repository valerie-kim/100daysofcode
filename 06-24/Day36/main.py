import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client
from datetime import date
from datetime import timedelta

# Stock
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"

# News
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# Twilio
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
client = Client(ACCOUNT_SID, AUTH_TOKEN)
MY_NUMBER = "<PUT YOUR NUMBER>"
VIRTUAL_TWILIO_NUMBER = "<TWILIO VIRTUAL NUMBER>"

url = f'https://www.alphavantage.co/query?function={FUNCTION}&symbol={STOCK}&apikey={STOCK_API_KEY}'
get_stock = requests.get(url)
stock_data = get_stock.json()
daily_stock = stock_data["Time Series (Daily)"]

# Get today and yesterday date
today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

# Get News 
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# Get the stock value of yesterday and today
yesterday_stock = float(daily_stock[str(yesterday)]['4. close'])
day_before_yesterday_stock = float(daily_stock[str(day_before_yesterday)]['4. close'])

# Compare the stock price if today's stock value increased/decreased 5% compared to yesterday.
# difference in percentage
difference = round((yesterday_stock-day_before_yesterday_stock)/((yesterday_stock+day_before_yesterday_stock)/2) * 100, 
                   2) # up to two decimals

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(difference) >= 5:
    every_news = newsapi.get_everything(q=COMPANY_NAME,
                                        from_param='2021-06-20',
                                        to='2021-06-23')
    three_articles = every_news["articles"][:3]
    for article in three_articles:
        title = article['title']
        content = article['content']
        url = article['url']
        message = client.messages \
            .create(
                    body= f'{STOCK}: {up_down}{abs(difference)}%\nTitle: {title}\nBreif: {content}\nURL: {url}',
                    from_=f'{VIRTUAL_TWILIO_NUMBER}',
                    to=f'{MY_NUMBER}'
            )