from pycoingecko import CoinGeckoAPI
from datetime import datetime
import pandas as pd

cg = CoinGeckoAPI()

def fetch_crypto_data(ids: list = ["bitcoin", "ethereum"]):
    data = []
    for crypto_id in ids:
        result = cg.get_price(ids=crypto_id, vs_currencies='usd', include_market_cap=True, include_24hr_change=True)
        data.append({
            'id': crypto_id,
            'symbol': crypto_id.upper(),
            'date': datetime.now(),
            'price': result[crypto_id]['usd'],
            'market_cap': result[crypto_id]['usd_market_cap'],
            'change_24h': result[crypto_id]['usd_24h_change']
        })
    return pd.DataFrame(data)
