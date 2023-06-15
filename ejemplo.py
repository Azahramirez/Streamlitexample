"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
    #cs_colbody()
    cs_body()
    

    return None

def cs_sidebar():
    url = "Imagen.png"
    st.sidebar.image(url, caption='Logo del equipo')
    st.sidebar.header('Para comunicarse con nosotros puede usar los siguientes medios')

    st.sidebar.markdown('''
<small>Gmail: [ServicIA@gmail.com](https://docs.streamlit.io/en/stable/api.html)</small>
    ''', unsafe_allow_html=True)

def cs_colbody():
    # Magic commands

    col1, col2, col3 = st.columns(3)

    col1.subheader('Magic commands')
    col1.code('''# Magic commands implicitly `st.write()`
    \'\'\' _This_ is some __Markdown__ \'\'\'
    a=3
    'dataframe:', data
    ''')

    # Display text

    col1.subheader('Display text')

    col2.subheader('Control flow')
    col2.code('''
    st.stop()
    ''')

    col3.subheader('Mutate data')

def cs_body():
    option=[0,0,0]
    option2=0

    st.write("<h1 style='text-align: center;'>Modelo predictivo de satisfacción en proyecto solidario</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center;'>Ranking mejores OSF por periodo</h2>", unsafe_allow_html=True)
    option2 = st.selectbox(
        'Métrica (promedio) a visualizar',
        ("sentimiento","sentimiento2","P1.1","P1.2","P1.3","P1.4","P1.5"))
    
    df = pd.read_csv("W2/DatosFinales.csv", encoding='utf-8')
    ranking = pd.read_csv("RankingFranco.csv", encoding='utf-8').drop(columns=["Unnamed: 0"],axis=1)
    ranking.index=ranking.index+1
    rankingM = pd.read_excel("RankingMalo.xlsx",engine='openpyxl').drop(columns=["Unnamed: 0"],axis=1)
    rankingM.index=rankingM.index+359

    col1, col2, col3 = st.columns(3)

    year_dict={"FJ21":'1',"VER21":'2',"AD21":'3',"FJ22":'4',"AD22":'5',"INV23":'6',"FJ23":'7'}
    def mostrarPeriodo(periodo,metrica):
        condition = df['Periodo']==periodo
        grupo=df[condition].groupby("OSF")[metrica].mean().sort_values(ascending=False)
        return grupo
    
        
    
    

    ## Repetir por columna---------------------------
    
    option[0] = col1.selectbox(
        'Número de primer periodo a visualizar',
        ("FJ21","VER21","AD21","FJ22","AD22","INV23","FJ23"))


    
    # Replace the string variable using the dictionary
    for key, value in year_dict.items():
        option[0] = (option[0]).replace(key, value)

    # Print the updated string
    option[0]=int(option[0])

    if int(option[0]) >0 and int(option[0])<8:
        primero=mostrarPeriodo(option[0],option2)
        col1.dataframe(primero)
        col1.bar_chart(primero)


    
    ## REPETIR POR COLUMNA------------------------
    ## Repetir por columna---------------------------
    option[1] = col2.selectbox(
        'Número de segundo periodo a visualizar',
        ("FJ21","VER21","AD21","FJ22","AD22","INV23","FJ23"))

    
    # Replace the string variable using the dictionary
    for key, value in year_dict.items():
        option[1] = (option[1]).replace(key, value)

    # Print the updated string
    option[1]=int(option[1])



    if int(option[1]) >0 and int(option[1])<8:
        segundo=mostrarPeriodo(option[1],option2)
        col2.dataframe(segundo)
        col2.bar_chart(segundo)

    
    ## REPETIR POR COLUMNA------------------------
    ## Repetir por columna---------------------------
    option[2] = col3.selectbox(
        'Número de tercer periodo a visualizar',
        ("FJ21","VER21","AD21","FJ22","AD22","INV23","FJ23"))

    
    # Replace the string variable using the dictionary
    for key, value in year_dict.items():
        option[2] = (option[2]).replace(key, value)

    # Print the updated string
    option[2]=int(option[2])
    ## Repetir por columna---------------------------

    

    if int(option[2]) >0 and int(option[2])<8:
        tercero=mostrarPeriodo(option[2],option2)
        col3.dataframe(tercero)
        col3.bar_chart(tercero)

    
    ## REPETIR POR COLUMNA------------------------
    #st.bar_chart()




    

    st.write("<h2 style='text-align: center;'>Ranking mejores OSF general (regresión lineal)</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    col1.table(ranking)

    option2 = col2.selectbox(
        'Mostrar resumen de comentarios',
        ("1","2","3","4","5","6","7","8","9","10"))

    option2=int(option2)


    direccion=("Nube"+str(option2-1)+".png")
    url2 = direccion
    cp= ('Palabras más comunes en OSF: '+ ranking["OSF"][option2])

    col2.image(url2, caption=cp)

    st.write("<h2 style='text-align: center;'>Ranking peores OSF general (regresión lineal)</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    col1.table(rankingM)

    option2 = col2.selectbox(
        'Mostrar resumen de comentarios malos',
        ("1","2","3","4","5","6","7","8","9","10"))

    option2=int(option2)


    direccion=("Mube"+str(option2-1)+".png")
    url2 = direccion
    cp= ('Palabras más comunes en OSF: '+ rankingM["OSF"][option2+359])

    col2.image(url2, caption=cp)


if __name__ == '__main__':
    main()
