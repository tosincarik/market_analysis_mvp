from supabase import create_client
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_stock_data(df):
    df = df.copy()
    
    # Convert datetime to string
    df['date'] = df['date'].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    # Replace problematic float values
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(0)  # or any default value you prefer

    # Insert into Supabase
    for _, row in df.iterrows():
        supabase.table("stocks_data").insert({
            "symbol": row['symbol'],
            "date": row['date'],
            "price": row['price'],
            "volume": row['volume'],
            "change_pct": row['change_pct']
        }).execute()



def insert_crypto_data(df):
    df = df.copy()
    
    # Convert datetime
    df['date'] = df['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S") if hasattr(x, 'strftime') else str(x))
    
    # Replace NaN/Inf
    import numpy as np
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(0)
    
    # Convert market_cap to int
    df['market_cap'] = df['market_cap'].astype(int)
    
    # Insert
    for _, row in df.iterrows():
        supabase.table("crypto_data").insert({
            "symbol": row['symbol'],
            "date": row['date'],
            "price": row['price'],
            "market_cap": row['market_cap'],
            "change_24h": row['change_24h']
        }).execute()

