"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write("<h1 style='text-align: center;'>Stream IA project</h1>", unsafe_allow_html=True)
url = "Streamlitexample/imagen.png"
st.image(url, caption='Logo del equipo')
st.write("<h2 style='text-align: left;'>Ranking mejores OSF</h2>", unsafe_allow_html=True)
dataframe = pd.read_excel("Streamlitexample/RankingFranco.xlsx")


st.dataframe(dataframe)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
