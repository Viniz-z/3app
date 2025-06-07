import streamlit as st

st.set_page_config(page_title="P-E", layout="centered")

st.markdown("<h1 style='text-align: center; font-family: Orbitron, sans-serif;'>P-E</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    time1 = st.text_input("", placeholder="Time 1")
with col2:
    time2 = st.text_input("", placeholder="Time 2")

if st.button("Comparar"):
    st.write(f"Você escolheu comparar: {time1} vs {time2}")
