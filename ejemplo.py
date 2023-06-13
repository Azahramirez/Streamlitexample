"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write("<h1 style='text-align: center;'>Stream IA project</h1>", unsafe_allow_html=True)
url = "Imagen.png"
st.image(url, caption='Logo del equipo')
st.write("<h2 style='text-align: left;'>Ranking mejores OSF</h2>", unsafe_allow_html=True)

# Upload the Excel file from the repository
uploaded_file = st.file_uploader("Upload Excel file")

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the Excel file data into a DataFrame
    df = pd.read_excel(uploaded_file)


st.dataframe(df)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
