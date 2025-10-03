import streamlit as st
import requests

st.title("MVP Dashboard - Week 1")

if st.button("Check API Health"):
    response = requests.get("http://127.0.0.1:8000/health")
    st.write(response.json())