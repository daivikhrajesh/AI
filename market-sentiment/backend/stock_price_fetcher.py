import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

if __name__ == "__main__":
    ticker = 'AAPL'
    data = fetch_stock_data(ticker)
    print(data.tail())
