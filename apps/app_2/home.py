import streamlit as st

# load css
css_path = Path(__file__).parent / "styles" / "template1_style.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("### Welcome to the Smart Scraping App", unsafe_allow_html=True)

st.markdown(
    """
        A simple platform to scrape, explore and analyze products from multiple online sources.
    """,
    unsafe_allow_html=True
)


# description
st.markdown("### What this app does")
st.markdown(
    """
    This application allows you to:
    
    👉 **Scrape product data** (clothes, shoes, etc.) from online marketplaces  especially **CoinAfrique platform**
    👉 **Perform quick analytics** on collected data  
    👉 **Download your datasets** for external use  
    👉 **Store and view your scraping history**  
    👉 **Give feedback** through evaluation forms (Google Form / KoboToolbox)
    
    """
)

st.markdown("")

# guide
st.markdown("### How to use the app")

col1, col2, col3 , col4= st.columns(4)

with col1:
    st.markdown("#### Scraping")
    st.markdown(
        """
        - Choose a product category  
        - Select page range  
        - Launch the scraper  
        """
    )

with col2:
    st.markdown("#### Analysis Dashboard")
    st.markdown(
        """
        - View product frequency  
        - Explore locations  
        - See top expensive items  
        """
    )

with col3:
    st.markdown("#### Download")
    st.markdown(
        """
        - Download all data of each category in only one click  
        """
    )

with col4:
    st.markdown("####  History")
    st.markdown(
        """
        - Track all past scraping operations  
        - Load old datasets  
        - Download previous results  
        """
    )


st.markdown("### How to start?", unsafe_allow_html=True)

st.markdown(
    """
       👉 Use the menu on the left to navigate between the different modules.
    """,
    unsafe_allow_html=True
)

st.markdown("### Evaluate the platform", unsafe_allow_html=True)

st.markdown(
    """
        Please fill our google form or kobotool form to help us to improve our app
    """,
    unsafe_allow_html=True
)

