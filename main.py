import sys
import yfinance as yf

def main():
    splg = yf.Ticker("SPLG")
    aapl = yf.Ticker("AAPL")
    msft = yf.Ticker("MSFT")
    print("SPLG Last Price: $" + str(round(splg.basic_info['lastPrice'], 2)))
    print("AAPL Last Price: $" + str(round(aapl.basic_info['lastPrice'], 2)))
    print("MSFT Last Price: $" + str(round(msft.basic_info['lastPrice'], 2)))

if __name__ == "__main__":
    main()