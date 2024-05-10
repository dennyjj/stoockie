import requests
import yfinance as yf
from tabulate import tabulate
from datetime import datetime, timezone
from config import get_config


def handler(event, context):
    try:
        config = get_config()
        telegram_base_url = config["telegram_base_url"]
        token = config["token"]
        chat_id = config["chat_id"]

        tickers = sorted(
            [get_ticker(ticker) for ticker in config["tickers"]],
            key=lambda ticker: ticker.ticker,
        )
        table = compose_stock_info_table(tickers)
        dt = datetime.now(timezone.utc)

        message = dt.strftime("%Y-%m-%d %A") + "\n" + table
        request_url = f"{telegram_base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

        requests.post(request_url)
        print(message)

    except Exception as e:
        print(e)
        return e


def get_ticker(symbol: str) -> yf.Ticker:
    return yf.Ticker(symbol)


def compose_stock_info_table(tickers: list[yf.Ticker]) -> str:
    header = ["Stock", "Price", "DH", "DL"]
    table = [header] + [compose_stock_info(ticker) for ticker in tickers]
    return tabulate(table, headers="firstrow", tablefmt="jira", numalign="left")


def compose_stock_info(ticker: yf.Ticker) -> list[str]:
    last_price = ticker.basic_info["lastPrice"]
    day_high = ticker.fast_info.day_high
    day_low = ticker.fast_info.day_low

    return [
        ticker.ticker,
        num_to_str(last_price),
        num_to_str(day_high),
        num_to_str(day_low),
    ]


def num_to_str(num: float) -> str:
    return str(round(num, 2))
