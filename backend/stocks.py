from yfinance import Ticker
import pandas as pd

def fetch_stock_data(symbol: str, period: str = "7d"):
    stock = Ticker(symbol)
    hist = stock.history(period=period)
    hist.reset_index(inplace=True)
    hist['symbol'] = symbol
    hist['change_pct'] = hist['Close'].pct_change() * 100
    hist = hist[['symbol', 'Date', 'Close', 'Volume', 'change_pct']]
    hist.rename(columns={'Date': 'date', 'Close': 'price', 'Volume': 'volume', 'change_pct': 'change_pct'}, inplace=True)
    return hist



