import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="P-E", layout="centered")

# Título com estilo futurista
st.markdown("<h1 style='text-align: center; font-family: monospace; color: #00f5ff;'>P-E</h1>", unsafe_allow_html=True)

# Entradas dos nomes dos times
col1, col2 = st.columns(2)
with col1:
    time1 = st.text_input("", placeholder="Time 1", label_visibility="collapsed")
with col2:
    time2 = st.text_input("", placeholder="Time 2", label_visibility="collapsed")

# Nomes dos quartos
quartos = ["Q1", "Q2", "Q3", "Q4"]
pontos_t1 = []
pontos_t2 = []

# Inputs dos pontos com chaves únicas e botões pequenos
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<h5 style='text-align:center'>{time1 or 'Time 1'}</h5>", unsafe_allow_html=True)
    for i, q in enumerate(quartos):
        ponto = st.number_input("", key=f"t1_q{i}", min_value=0, step=1, label_visibility="collapsed")
        pontos_t1.append(ponto)

with col2:
    st.markdown(f"<h5 style='text-align:center'>{time2 or 'Time 2'}</h5>", unsafe_allow_html=True)
    for i, q in enumerate(quartos):
        ponto = st.number_input("", key=f"t2_q{i}", min_value=0, step=1, label_visibility="collapsed")
        pontos_t2.append(ponto)

# Mostrar gráfico se todos os campos forem preenchidos
if all(isinstance(p, int) for p in pontos_t1 + pontos_t2):
    df = pd.DataFrame({
        "Quarto": quartos,
        time1 or "Time 1": pontos_t1,
        time2 or "Time 2": pontos_t2
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(x=quartos, y=pontos_t1, name=time1 or "Time 1"))
    fig.add_trace(go.Bar(x=quartos, y=pontos_t2, name=time2 or "Time 2"))

    fig.update_layout(
        barmode='group',
        title="Comparação por Quarto",
        xaxis_title="Quarto",
        yaxis_title="Pontos",
        template="plotly_dark"
    )

    st.plotly_chart(fig)
