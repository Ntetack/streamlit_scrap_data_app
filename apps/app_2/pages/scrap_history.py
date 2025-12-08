import streamlit as st
import pandas as pd
import sqlite3
import os

css_file = "styles/template1_style.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;'>Scraping history</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Here is the list of last scraping by users. You can directly download it or show visualisation about it.</p>", unsafe_allow_html=True)

# verify if database exist
if not os.path.exists("scraped_data.db"):
    st.warning("No database")
else:
    conn = sqlite3.connect("scraped_data.db")
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()

    # Lister tous les scraping_id existants
    scrapings = df['scraping_id'].unique()

    for sid in scrapings:
        st.markdown(f"##### Description: {df[df['scraping_id'] == sid]['description'].unique()[0]}")
        st.markdown(f"({df.shape[0]} rows x {df.shape[1]} columns)")
        st.dataframe(df[df['scraping_id'] == sid])


  
