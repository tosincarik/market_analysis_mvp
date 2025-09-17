# config.py
import os
import urllib
from sqlalchemy import create_engine

# API Keys
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Test tickers
TICKERS = ["AAPL", "BTC"]

# SQL Server connection
params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=OLUWATOSIN,1433;"
    "Database=MarketMVP;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

DB_CONNECTION_STRING = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(DB_CONNECTION_STRING)

# Test connection function
def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("SQL Server connection successful:", result.fetchone())
    except Exception as e:
        print("SQL Server connection failed:", e)

if __name__ == "__main__":
    test_connection()
