import os
import requests
import yfinance as yf


def handler():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    ticker_one = yf.Ticker(os.getenv('TICKER_ONE'))
    ticker_two = yf.Ticker(os.getenv('TICKER_TWO'))
    ticker_three = yf.Ticker(os.getenv('TICKER_THREE'))
    ticker_four = yf.Ticker(os.getenv('TICKER_FOUR'))
    ticker_five = yf.Ticker(os.getenv('TICKER_FIVE'))

    printTicker(ticker_one)
    printTicker(ticker_two)
    printTicker(ticker_three)
    printTicker(ticker_four)
    printTicker(ticker_five)

    message = "hello from telegram bot"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    return requests.get(url).json()


def printTicker(ticker):
    print(ticker.ticker + " Last Price: " +
          str(round(ticker.basic_info['lastPrice'], 2)))


if __name__:
    handler()
