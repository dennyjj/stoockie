import requests
import yfinance as yf

from config import get_config


def handler(event, context):
    try:
        config = get_config()

        token = config['token']
        chat_id = config['chat_id']

        tickers = [get_ticker(ticker) for ticker in config['tickers']]
        message = compose_telegram_message(tickers)
        print(message)

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

    except Exception as e:
        print(e)


def get_ticker(symbol):
    return yf.Ticker(symbol)


def compose_telegram_message(tickers):
    return "\n".join([compose_last_price_message(ticker) for ticker in tickers])


def compose_last_price_message(ticker):
    return (ticker.ticker + " Last Price: " +
            num_to_str(ticker.basic_info['lastPrice']))


def num_to_str(num):
    return str(round(num, 2))
