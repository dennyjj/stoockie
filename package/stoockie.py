import requests
import yfinance as yf
from tabulate import tabulate

from config import get_config


def handler(event, context):
    try:
        config = get_config()

        token = config["token"]
        chat_id = config["chat_id"]

        tickers = [get_ticker(ticker) for ticker in config["tickers"]]
        message = compose_telegram_message(tickers)
        print(message)

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

    except Exception as e:
        print(e)


def get_ticker(symbol):
    return yf.Ticker(symbol)


def compose_telegram_message(tickers):
    header = ["Stock", "Price", "DH", "DL"]
    table = [header] + [compose_stock_message(ticker) for ticker in tickers]
    return tabulate(table, headers="firstrow", tablefmt="jira", numalign="left")


def compose_stock_message(ticker):
    last_price = ticker.basic_info["lastPrice"]
    day_high = ticker.fast_info.day_high
    day_low = ticker.fast_info.day_low

    return [
        ticker.ticker,
        num_to_str(last_price),
        num_to_str(day_high),
        num_to_str(day_low),
    ]


def num_to_str(num):
    return str(round(num, 2))
