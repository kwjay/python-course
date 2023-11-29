import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "",
}
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "apiKey": "",
}
NEWS_URL = "https://newsapi.org/v2/everything"


def get_news():
    news_response = requests.get(NEWS_URL, NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    for news in news_data["articles"]:
        print(f"{news["title"]}\n{news["description"]}")



STOCK_URL = "https://www.alphavantage.co/query"
stock_response = requests.get(STOCK_URL, STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()
dates = list(stock_data["Time Series (Daily)"].keys())
yesterday = dates[0]
day_before = dates[1]
yesterday_price = stock_data["Time Series (Daily)"][yesterday]["4. close"]
day_before_price = stock_data["Time Series (Daily)"][day_before]["4. close"]
difference = yesterday_price/day_before_price * 100
if 95 < difference or difference > 105:
    print(f"TSLA: {difference}")
    get_news()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

