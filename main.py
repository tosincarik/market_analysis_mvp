import sys
import os
import streamlit as st

# Ensure backend modules are found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Backend imports
from backend.stocks import fetch_stock_data
from backend.crypto import fetch_crypto_data
from backend.supabase_client import insert_stock_data, insert_crypto_data

# ----------------- Streamlit App -----------------
st.title("Stock & Crypto Dashboard – Week 2 Test")

# ----- User Input -----
st.subheader("Fetch Stock Data")
stock_symbol = st.text_input("Enter a stock symbol", "AAPL")
stock_period = st.selectbox("Select period", ["7d", "30d", "90d"], index=0)

st.subheader("Crypto Data")
crypto_symbols_input = st.text_area(
    "Enter crypto IDs separated by commas",
    "bitcoin,ethereum"
)
crypto_symbols = [s.strip() for s in crypto_symbols_input.split(",")]

# ----------------- Stock Data -----------------
if st.button("Fetch Stock Data"):
    try:
        stock_df = fetch_stock_data(stock_symbol, stock_period)
        st.subheader(f"Stock Data – {stock_symbol}")
        st.dataframe(stock_df)
        insert_stock_data(stock_df)
        st.success(f"Stock data for {stock_symbol} inserted into Supabase!")
    except Exception as e:
        st.error(f"Error fetching/inserting stock data: {e}")



# ----------------- Crypto Data -----------------
if st.button("Fetch Crypto Data"):
    try:
        crypto_df = fetch_crypto_data(crypto_symbols)
        st.subheader("Crypto Data")
        st.dataframe(crypto_df)
        insert_crypto_data(crypto_df)
        st.success("Crypto data inserted into Supabase!")
    except Exception as e:
        st.error(f"Error fetching/inserting crypto data: {e}")

# ----------------- Full Test Button -----------------
if st.button("Run Full Test"):
    try:
        # Stocks
        stock_df = fetch_stock_data("AAPL", "7d")
        insert_stock_data(stock_df)
        st.subheader("Stock Data – AAPL")
        st.dataframe(stock_df)

        # Crypto
        crypto_df = fetch_crypto_data(["bitcoin", "ethereum"])
        insert_crypto_data(crypto_df)
        st.subheader("Crypto Data")
        st.dataframe(crypto_df)

        st.success("✅ Full test completed: all data fetched and inserted!")
    except Exception as e:
        st.error(f"Error during full test: {e}")
