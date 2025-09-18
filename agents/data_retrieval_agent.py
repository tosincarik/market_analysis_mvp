# agents/data_retrieval_agent.py
import yfinance as yf
from pycoingecko import CoinGeckoAPI

class DataRetrievalAgent:
    def __init__(self, stocks=[], cryptos=[]):
        self.stocks = stocks
        self.cryptos = cryptos
        self.cg = CoinGeckoAPI()

    def fetch_stocks(self):
        data_dict = {}
        for ticker in self.stocks:
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(period="5d")  # last 5 days
                data_dict[ticker] = hist.to_dict()
            except Exception as e:
                print(f"Error fetching {ticker}: {e}")
        return data_dict

    def fetch_cryptos(self):
        data_dict = {}
        for coin in self.cryptos:
            try:
                data = self.cg.get_coin_market_chart_by_id(id=coin.lower(), vs_currency='usd', days=5)
                data_dict[coin] = data
            except Exception as e:
                print(f"Error fetching {coin}: {e}")
        return data_dict

    def fetch(self):
        # Combine both
        return {**self.fetch_stocks(), **self.fetch_cryptos()}

# Test block
if __name__ == "__main__":
    agent = DataRetrievalAgent(stocks=["AAPL"], cryptos=["bitcoin"])
    print(agent.fetch())






