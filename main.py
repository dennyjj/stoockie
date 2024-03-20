import sys
import yfinance as yf

def main():
    ticker_symbol = sys.argv[1].upper()
    ticker = yf.Ticker(ticker_symbol)
    print("Last Price: $" + str(round(ticker.basic_info['lastPrice'], 2)))

if __name__ == "__main__":
    main()