import streamlit as st
import pandas as pd
import os
from pathlib import Path

# load css
css_file = Path(__file__).parent / "styles" / "template1_style.css"


with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h2>Donwload data</h2>", unsafe_allow_html=True)

st.markdown("""
This data set had been extracted from web site https://sn.coinafrique.com 
It contain product category such that clothes, shoes for children and men.
""")

# sidebar
st.sidebar.markdown("<h4>Available data<h4>", unsafe_allow_html=True)
csv_files = [
    ("Child clothes", Path(__file__).parent / "data" / "vetement-enfant.csv"),
    ("Man clothes", Path(__file__).parent / "data" / "vetement-homme.csv"),
    ("Child shoes", Path(__file__).parent / "data" / "chaussure-enfant.csv"),
    ("Man shoes", Path(__file__).parent / "data" / "chaussure-homme.csv")
]

menu_selection = st.sidebar.radio("Choose a dataset:", [name for name, _ in csv_files])

# data frame
for name, path in csv_files:
    if menu_selection == name:
        df = pd.read_csv(path)
        st.subheader(f"{name} ({df.shape[0]} rows x {df.shape[1]} columns)")
        st.dataframe(df)
        # download button
        st.sidebar.download_button(
            label=f"Download",
            data=open(path, "rb").read(),
            file_name=os.path.basename(path),
            mime="text/csv"
        )
        break
