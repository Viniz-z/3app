import streamlit as st
import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Previsor de Quebra", layout="centered")

st.title("🎾 Previsor de Quebra de Serviço - Tênis")

st.markdown("""
Cole abaixo os dados da partida no formato CSV com as colunas:  
`game_id,server,receiver,server_points,receiver_points,server_aces,server_double_faults,server_1st_serve_pct,game_winner,break_occurred`
""")

exemplo_csv = """game_id,server,receiver,server_points,receiver_points,server_aces,server_double_faults,server_1st_serve_pct,game_winner,break_occurred
1,Nadal,Djokovic,4,2,1,0,68,Nadal,0
2,Djokovic,Nadal,2,4,2,1,62,Nadal,1
3,Nadal,Djokovic,4,0,0,0,74,Nadal,0
4,Djokovic,Nadal,3,5,1,2,59,Nadal,1
5,Nadal,Djokovic,1,4,0,1,63,Djokovic,1
6,Djokovic,Nadal,4,0,3,0,70,Djokovic,0
7,Nadal,Djokovic,2,4,1,2,66,Djokovic,1
"""

data_input = st.text_area("📋 Cole os dados aqui (formato CSV)", value=exemplo_csv, height=250)

if st.button("Analisar dados"):

    if not data_input.strip():
        st.error("⚠️ Por favor, cole os dados antes de analisar!")
    else:
        try:
            data = pd.read_csv(StringIO(data_input))
            st.success("✅ Dados carregados com sucesso!")
            st.write("Prévia dos dados:")
            st.dataframe(data.head())

            features = ['server_points', 'receiver_points', 'server_aces', 'server_double_faults', 'server_1st_serve_pct']
            X = data[features]
            y = data['break_occurred']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            model = LogisticRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            st.write(f"📊 **Acurácia do modelo:** {acc:.2f}")

            st.write("🔎 Relatório de classificação:")
            st.text(classification_report(y_test, y_pred))

            coef = pd.Series(model.coef_[0], index=features)
            st.write("📈 Importância das variáveis:")
            st.bar_chart(coef)

            st.write("🧪 Mapa de calor das correlações:")
            plt.figure(figsize=(8,6))
            sns.heatmap(data[features + ['break_occurred']].corr(), annot=True, cmap='coolwarm')
            st.pyplot(plt)

        except Exception as e:
            st.error(f"❌ Erro ao processar os dados: {e}")
