import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="P-E", layout="centered")
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #0f1117;
            color: white;
            font-family: 'Orbitron', sans-serif;
        }
        .title {
            font-size: 3em;
            text-align: center;
            color: #00ffe7;
            margin-bottom: 30px;
        }
        .stTextInput>div>div>input {
            height: 30px;
            font-size: 16px;
            text-align: center;
        }
        .stButton>button {
            height: 32px;
            padding: 0 12px;
            font-size: 14px;
            border-radius: 8px;
            background-color: #1e1e2f;
            color: white;
            font-weight: bold;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='title'>P-E</div>", unsafe_allow_html=True)

# Times
col1, col2 = st.columns(2)
with col1:
    time1 = st.text_input("", placeholder="Time 1")
with col2:
    time2 = st.text_input("", placeholder="Time 2")

# Digitar Pontos por Quarto
quartos = ["Q1", "Q2", "Q3", "Q4"]
pontos_t1 = []
pontos_t2 = []

st.markdown("")

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"##### {time1 or 'Time 1'}")
    for q in quartos:
        ponto = st.number_input(f"{q}", key=f"{time1}_{q}", min_value=0, step=1)
        pontos_t1.append(ponto)

with col2:
    st.markdown(f"##### {time2 or 'Time 2'}")
    for q in quartos:
        ponto = st.number_input(f"{q}", key=f"{time2}_{q}", min_value=0, step=1)
        pontos_t2.append(ponto)

# Botão Comparar
if st.button("Comparar"):
    df = pd.DataFrame({
        "Quarto": quartos * 2,
        "Pontos": pontos_t1 + pontos_t2,
        "Time": [time1] * 4 + [time2] * 4
    })

    fig = px.bar(df, x="Quarto", y="Pontos", color="Time", barmode="group",
                 title=f"{time1} vs {time2}", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
