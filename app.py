import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de Análise de Veículos 🚗")


df = pd.read_csv("vehicles.csv")

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma da quilometragem dos veículos')
    
    fig_hist = px.histogram(
        df, 
        x='odometer',
        title= 'Distribuição da Quilometragem (odometro)'
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)
    
    
disp_button = st.button("Dispersão (Preço vs Odômetro)")

if disp_button:
    st.write('Criando gráfico de dispersão entre preço e quilometragem')
    
    fig = px.scatter(
            df,
            x='odometer',
            y='price',
            title="Preço vs Quilometragem",
            opacity=0.5
    )
    
    st.plotly_chart(fig, use_container_width=True)