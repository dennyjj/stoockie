import yfinance as yf
import os


def handler(event, context):
    ticker_one = yf.Ticker(os.getenv('TICKER_ONE'))
    ticker_two = yf.Ticker(os.getenv('TICKER_TWO'))
    ticker_three = yf.Ticker(os.getenv('TICKER_THREE'))
    ticker_four = yf.Ticker(os.getenv('TICKER_FOUR'))
    ticker_five = yf.Ticker(os.getenv('TICKER_FIVE'))

    print(ticker_one.ticker + " Last Price: " +
          str(round(ticker_one.basic_info['lastPrice'], 2)))
    print(ticker_two.ticker + " Last Price: " +
          str(round(ticker_two.basic_info['lastPrice'], 2)))
    print(ticker_three.ticker + " Last Price: " +
          str(round(ticker_three.basic_info['lastPrice'], 2)))
    print(ticker_four.ticker + " Last Price: " +
          str(round(ticker_four.basic_info['lastPrice'], 2)))
    print(ticker_five.ticker + " Last Price: " +
          str(round(ticker_five.basic_info['lastPrice'], 2)))
