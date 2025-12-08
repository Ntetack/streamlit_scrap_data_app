import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import unidecode
from pathlib import Path

# load css
css_file = Path(__file__).parent / "styles" / "template1_style.css"

st.markdown("<h2>Dashboard</h2>", unsafe_allow_html=True)
st.markdown("This shows short analysis on data available in our app.")


#precess text
def clean_article_type(text):
    if pd.isna(text):
        return text
    text = text.lower().strip()                  # minuscules et enlever espaces
    text = unidecode.unidecode(text)            # enlever accents
    words = text.split()                         
    words = [w[:-1] if w.endswith('s') else w for w in words]  # supprimer 's' final
    return ' '.join(words)

#build graphics
def data_ploting(df):
    #choose column
    df = df[['price', 'article_type', 'address']]

    #process price
    df = df.dropna().drop_duplicates()
    df['price'] = df['price'].str.replace('CFA', '').str.replace(' ', '')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna()

    #process article
    df['article_type'] = df['article_type'].apply(clean_article_type)

    #build graphics
    
    colors = ['blue', 'red', 'green', 'orange', 'purple']

    # Top 5 products in stock
    top5_in_stock = df['article_type'].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8,5))
    top5_in_stock.plot(kind='bar', color=colors, ax=ax)
    ax.set_title("Top 5 products in stock")
    ax.set_ylabel("Nombre")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
    st.pyplot(fig)  # <- afficher le graphique dans Streamlit

    # Top 5 locations
    top5_address = df['address'].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8,5))
    top5_address.plot(kind='bar', color=colors, ax=ax)
    ax.set_title("Top 5 locations")
    ax.set_ylabel("Nombre")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
    st.pyplot(fig)

    # Top 5 expensive products
    top5_expensive = df[['article_type', 'price']].set_index('article_type').sort_values('price', ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(8,5))
    top5_expensive.plot(kind='bar', color=colors, legend=False, ax=ax)
    ax.set_title("Top 5 Expensive Products")
    ax.set_ylabel("Price (CFA)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig)

# Sidebar
st.sidebar.markdown("<h4>Available data</h4>", unsafe_allow_html=True)
csv_files = [
    ("Child clothes", Path(__file__).parent / "data" / "vetement-enfant"),
    ("Man clothes", "data/vetement-homme.csv"),
    ("Child shoes", "data/chaussure-enfant.csv"),
    ("Man shoes", "data/chaussure-homme.csv")
]

menu_selection = st.sidebar.radio("Choose a dataset:", [name for name, _ in csv_files])

# Load and plot
for name, path in csv_files:
    if menu_selection == name:
        df = pd.read_csv(path)
        data_ploting(df)
        break
