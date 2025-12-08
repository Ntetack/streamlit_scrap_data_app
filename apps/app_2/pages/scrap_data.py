# import packages
from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import streamlit as st
from database import create_table, save_to_db


# load css
css_file = "styles/template1_style.css" 
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#create database and table if not exist
create_table()

#scraping fonction
def scrap_article(article_type, first_page, last_page):
    if(article_type=='man clothes'):
        page_link = 'https://sn.coinafrique.com/categorie/vetements-homme'
    elif(article_type=='man shoes'):
        page_link  ='https://sn.coinafrique.com/categorie/chaussures-homme'
    elif(article_type=='child clothes'):
        page_link ='https://sn.coinafrique.com/categorie/vetements-enfants'
    elif(article_type=='child shoes'):
        page_link ='https://sn.coinafrique.com/categorie/chaussures-enfants'
    else:
        print()
    

    all_data=[]
    for i in range(first_page,1+last_page):
        
        url = page_link + '?page={i}'
        # get the code
        res = get(url)
        # store the code in a Beautifulsoup objet
        soup = bs(res.content, 'html.parser')
        #print(soup)
        # find containers
        containers = soup.find_all("div", class_="col s6 m4 l3")
        #print('#########' , containers)

        for c in containers:
            #details = c.find('p', 'ad__card-description').text.strip()
            try:
                price = ''.join(c.find('p', 'ad__card-price').find('a').text.strip().replace('CFA', '').split())
                adress = c.find('p', 'ad__card-location').find('span').text
                img_link = c.find("img", class_="ad__card-img")["src"]
                #part_link = c.find('p', 'ad__card-description').find('a')['href'] 
                #sub_link = 'https://ci.coinafrique.com'+part_link
                article = c.find('p', 'ad__card-description').find('a').text
                dic = {
                    'article': article,
                    'adress':adress,
                    "price": price,
                    'img_link': img_link,

                }
                all_data.append(dic)

            except:
                pass


    df = pd.DataFrame(all_data)
    df['description'] = f'article type: {article_type}, first page: {first_page}, last_page: {last_page}'
    
    return df




#title
st.markdown("<h1>Scraping Configuration</h1>", unsafe_allow_html=True)

with st.form(key="scraping_form"):
    # article type
    article_type = st.selectbox(
        "Select the type of article to scrape:",
        options=['child clothes','man clothes', 'child shoes', 'man shoes'],
        index=0  
    )
    
    # begin
    first_page = st.number_input(
        "First page to scrape:",
        min_value=1,
        max_value=100,
        value=1 
    )
    
    # end
    last_page = st.number_input(
        "Last page to scrape:",
        min_value=1,
        max_value=100,
        value=5  # default
    )
    

    submit_button = st.form_submit_button(label="Start Scraping")



# start scaping
if submit_button:
    with st.spinner("Scraping in progress..."):
        df = scrap_article(article_type, first_page, last_page)
    
    st.success("Scraping finished!")
    save_to_db(df)
    st.write(f"Displaying {len(df)} items scraped from {article_type}")
    csv = df.to_csv(index=False)

    # download button
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="scraped_data.csv",
        mime="text/csv"
    )
    st.dataframe(df.drop(columns={'description'}))



