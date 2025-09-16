import streamlit as st
import requests

st.title("Market Dashboard MVP")

symbol = st.text_input("Ticker (e.g. AAPL, BTC):", "AAPL")
if st.button("Check Price"):
    resp = requests.get("http://127.0.0.1:8000/health")
    st.json(resp.json())
