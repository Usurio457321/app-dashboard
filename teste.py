import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('base_rh.csv')

st.title('Dashboard RH')

def constroi_grafico_barras(variavel):
    contagem = df[variavel].value_counts().reset_index()
    contagem.columns = [variavel, 'Contagem']  # Renomeia as colunas
    
    fig = px.bar(contagem, x=variavel, y='Contagem', title='Qtd de Funcionários por ' + variavel, text_auto=True) 
    return fig


col1, col2,col3 = st.columns(3)    

grafico1 = constroi_grafico_barras('Estado_Civil')
col1.plotly_chart(grafico1)

grafico2 = constroi_grafico_barras('Formacao')
col2.plotly_chart(grafico2)

grafico3 = constroi_grafico_barras('Freq_Viagens')
col2.plotly_chart(grafico3)