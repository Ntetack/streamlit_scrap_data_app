import streamlit as st
import pandas as pd
import os

css_file = "styles/template1_style.css" 
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

google_form_link = "https://tinyurl.com/y2sf5c2n"
kobo_form_link = "https://ee.kobotoolbox.org/x/vCRrIqqp"

st.markdown("<h2 style='text-align:center;'>Evaluation Page</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Please fill a form to help us improve our app.</p>", unsafe_allow_html=True)

st.markdown("Choose one platform:")

st.markdown(
    f"<b>👉 Google Form</b>: <a href='{google_form_link}' target='_blank'>{google_form_link}</a>",
    unsafe_allow_html=True
)

st.markdown(
    f"<b>👉 KoboToolbox</b>: <a href='{kobo_form_link}' target='_blank'>{kobo_form_link}</a>",
    unsafe_allow_html=True
)


