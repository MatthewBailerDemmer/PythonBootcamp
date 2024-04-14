STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = "ZZYP4I5FA2MBDRDO"
NEWS_API_KEY = "905b49ef05e04be3a8a9d6c87ecb710f"
import datetime
from twilio.rest import Client
account_sid = "AC3bd1d9b23ff95534f7212e524abd3b36"
auth_token = "efc8808667bdb9ae790729df0d07da5a"

import requests

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news():
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",
        "category": "business",
        "q": "Tesla"
    }
    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=params)
    return (response.json()["totalResults"], response.json()["articles"])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_news_message():
    news = get_news()
    client = Client(account_sid, auth_token)
    number_of_messages = 0
    if news[0] > 0 and number_of_messages <= 3:
        for i in news[1]:
            message = client.messages.create(
                from_="+12679332335",
                body=f"{STOCK}: {emoji}{percentage}%\nHeadline: {i["title"]}\nBrief: {i["description"]}",
                to="+447927462101",
            )
            print(message.status)
            number_of_messages += 1
    else:
        message = client.messages.create(
            from_="+12679332335",
            body=f"{STOCK}: {emoji}{percentage}%\nNo news",
            to="+447927462101",
        )

## STEP 1: Use https://www.alphavantage.co
## When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
previous =  str(datetime.date.today() - datetime.timedelta(days=2))
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY,
}
response = requests.get("https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()
yesterday_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
previous_price = float(data["Time Series (Daily)"][previous]["4. close"])
difference = yesterday_price - previous_price
emoji = difference > 0 and "🔺" or "🔻"
percentage = int(abs(difference) * 100/previous_price)
if percentage >= 5:
    send_news_message()
else:
    print("The difference is not over 5%")






#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

