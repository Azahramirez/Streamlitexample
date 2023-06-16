"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('treeModel.pkl','rb'))


st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
  
    cs_body()
    

    return None

def predict_P1(a):
    #input=np.array([[a,b]]).astype(np.float64)
    input=a.astype(np.float64)

    prediction = model.predict(input)
    
    return int(prediction)

def cs_sidebar():
    url = "Imagen.png"
    st.sidebar.image(url, caption='Logo del equipo')
    st.sidebar.header('Para comunicarse con nosotros puede usar los siguientes medios')

    st.sidebar.markdown('''
<small>Gmail: [ServicIA@gmail.com](https://docs.streamlit.io/en/stable/api.html)</small>
    ''', unsafe_allow_html=True)



def cs_body():
    URL = "Portada.png"
    st.image(URL, caption='Equipo 2')


    option=[0,0,0]
    option2=0

    st.write("<h1 style='text-align: center;'>Modelo predictivo de satisfacción en proyecto solidario</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center;'>Ranking mejores OSF por periodo</h2>", unsafe_allow_html=True)
    option2 = st.selectbox(
        'Métrica (promedio) a visualizar',
        ("sentimiento","sentimiento2","P1.1","P1.2","P1.3","P1.4","P1.5"))
    
    df = pd.read_csv("DatosFinales.csv", encoding='utf-8')
    ranking = pd.read_csv("RankingFranco.csv", encoding='utf-8').drop(columns=["Unnamed: 0"],axis=1)
    ranking.index=ranking.index+1
    rankingM = pd.read_csv("RankingMalo.csv", encoding='utf-8').drop(columns=["Unnamed: 0"],axis=1)
    rankingM.index=rankingM.index+359
    labels = pd.read_csv("ClusterOSF.csv", encoding='utf-8')
    df["OSFtype"]=labels["OSFtype"]

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
        ("1","2","3","4","5","6","7","8","9"))

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
        ("1","2","3","4","5","6","7","8","9"))

    option2=int(option2)


    direccion=("Mube"+str(option2-1)+".png")
    url2 = direccion
    cp= ('Palabras más comunes en OSF: '+ rankingM["OSF"][option2+359])

    col2.image(url2, caption=cp)

    
    
    #Predicciones y recomendaciones
    st.write("<h2 style='text-align: center;'>Predicción y recomendación</h2>", unsafe_allow_html=True)

    # Tabla del performace de los grupos
    st.write("<h3 style='text-align: center;'>Tabla de grupos encontrados usando clustering</h2>", unsafe_allow_html=True)
    col1, col2 ,col3= st.columns(3)
    data = {'cluster': ['Grupo0', 'Grupo1', 'Grupo2'],
        'Cantida de registros': [6709, 3086, 698],
        'Calidad':['Excelente','Bueno','Malo']}
    dfG=pd.DataFrame(data)
    col2.dataframe(dfG)


    

    #Arbol de decision
    #[["P1.2", "P1.3", "P1.4", "P1.5", "P1.6", "P1.7", "P2", "P3", "P5.1", "P5.2", "P5.3", "P5.4","sentimiento","sentimiento2"]].values 
    def selRandom(cluster):
        pas=labels.loc[labels["OSFtype"]==cluster]
        e=np.array(pas.index)
        random_e=np.random.choice(e)
        return random_e

    def select(num):
        seleccion=df.loc[num]
        seleccion=pd.DataFrame(seleccion)
        seleccion=seleccion.transpose()
        W = seleccion[["P1.2", "P1.3", "P1.4", "P1.5", "P1.6", "P1.7", "P2", "P3", "P5.1", "P5.2", "P5.3", "P5.4","sentimiento","sentimiento2"]].values
        return W
    
    def comentario(grupo):
        if grupo==0:
            num=4818
        if grupo==1:
            num=1293
        if grupo==2:
            num=3058


        W=df["Comentario para OSF"][num]
        H=df["OSF"][num]
        return W,H
    
    def encontrar(clus):
        muestra=selRandom(int(clus)) 
        p=select(muestra)
        p=predict_P1(p)
        com,OSF=comentario(int(clus))
        val=("Nivel: "+str(p))
        delt=str(df["P1.1"][muestra]-p)
        deltax=(delt+" = Diferencia con real ("+str(df["P1.1"][muestra])+")")
        return muestra,p,com,OSF,val,delt,deltax
    
    def mostrarGrupo(grupo):
        condition = df['OSFtype']==grupo
        G=df[condition].head(5)
        Grupo=df[condition].groupby("P1.1")["P1.3"].count().sort_values(ascending=False)
        Grupo=pd.DataFrame(Grupo)
        Grupo["P1.1"]=Grupo.index
        Grupo.reset_index(drop=True,inplace=True)
        Grupo["P1"]=Grupo["P1.1"].astype(str)
        Grupo["cantidad"]=Grupo["P1.3"].astype(int)
        Grupo = Grupo[['P1', 'cantidad']]
        return Grupo,G
    
    col1, col2 ,col3= st.columns(3)
    
    ##==========Repetir por columna======================================================
    cluster1 = col1.selectbox(
        'Grupo de la muestra1',
        ("0","1","2"))
    muestra,p,com,OSF,val,delt,deltax = encontrar(cluster1)
    col1.metric(label="Satisfacción predecida", value=val, delta=deltax ,delta_color="off")
    col1.write("Comentario centroide del grupo:")
    col1.text(com, help=("Comentario de OSF centroide: "+OSF))
    pri,prit=mostrarGrupo(int(cluster1))
    col1.write("Satisfacción en el grupo:")
    col1.bar_chart(pri,x='P1',y='cantidad')
    col1.write("Más experiencias del grupo:")
    col1.dataframe(prit)
    #===========================================================================================
    ##==========Repetir por columna======================================================
    cluster2 = col2.selectbox(
        'Grupo de la muestra2',
        ("0","1","2"))
    muestra,p,com,OSF,val,delt,deltax = encontrar(cluster2)
    col2.metric(label="Satisfacción predecida", value=val, delta=deltax ,delta_color="off")
    col2.write("Comentario centroide del grupo:")
    col2.text(com, help=("Comentario de OSF centroide: "+OSF))
    pri,prit=mostrarGrupo(int(cluster2))
    col2.write("Satisfacción en el grupo:")
    col2.bar_chart(pri,x='P1',y='cantidad')
    col2.write("Más experiencias del grupo:")
    col2.dataframe(prit)
    #===========================================================================================
    ##==========Repetir por columna======================================================
    cluster3 = col3.selectbox(
        'Grupo de la muestra3',
        ("0","1","2"))
    muestra,p,com,OSF,val,delt,deltax = encontrar(cluster3)
    col3.metric(label="Satisfacción predecida", value=val, delta=deltax ,delta_color="off")
    col3.write("Comentario centroide del grupo:")
    col3.text(com, help=("Comentario de OSF centroide: "+OSF))
    pri,prit=mostrarGrupo(int(cluster3))
    col3.write("Satisfacción en el grupo:")
    col3.bar_chart(pri,x='P1',y='cantidad')
    col3.write("Más experiencias del grupo:")
    col3.dataframe(prit)
    #===========================================================================================
    st.image(URL)
    
    




if __name__ == '__main__':
    main()
