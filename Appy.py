import streamlit as st
import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Quebra de Serviço - Tênis", layout="wide")

st.title("🎾 Previsor de Quebra de Serviço no Tênis")

st.markdown("Cole os dados ou envie um CSV com estatísticas dos games para analisar quebras de serviço e padrões.")

tab1, tab2, tab3 = st.tabs(["📄 Inserir Dados", "📊 Análise", "📈 Visualização"])

with tab1:
    data_input = st.text_area("📥 Cole os dados CSV aqui:", height=200)

    uploaded_file = st.file_uploader("📁 Ou envie um arquivo CSV", type=["csv"])

    if uploaded_file:
        try:
            data = pd.read_csv(uploaded_file)
            st.success("Arquivo carregado com sucesso!")
        except:
            st.error("Erro ao ler o arquivo.")
            data = None
    elif data_input.strip():
        try:
            data = pd.read_csv(StringIO(data_input))
            st.success("Dados colados com sucesso!")
        except:
            st.error("Erro ao processar os dados colados.")
            data = None
    else:
        data = None

    if data is not None:
        st.dataframe(data.head())

with tab2:
    if data is not None:
        try:
            features = ['server_points', 'receiver_points', 'server_aces', 'server_double_faults', 'server_1st_serve_pct']
            X = data[features]
            y = data['break_occurred']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            model = LogisticRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]

            acc = accuracy_score(y_test, y_pred)

            st.subheader("🔍 Resultados do Modelo")
            st.write(f"**Acurácia:** {acc:.2%}")
            st.text("Relatório de Classificação:")
            st.text(classification_report(y_test, y_pred))

            # Probabilidade de quebra para cada game no teste
            result_df = X_test.copy()
            result_df["Probabilidade de Quebra"] = y_proba
            result_df["Previsto: Quebra"] = y_pred
            st.write("📌 Previsões:")
            st.dataframe(result_df.reset_index(drop=True))

        except Exception as e:
            st.error(f"Erro ao analisar os dados: {e}")
    else:
        st.warning("🔁 Insira os dados na aba anterior para continuar.")

with tab3:
    if data is not None:
        try:
            st.subheader("📊 Mapa de Correlação entre Variáveis")
            features_corr = ['server_points', 'receiver_points', 'server_aces', 'server_double_faults', 'server_1st_serve_pct', 'break_occurred']
            corr = data[features_corr].corr()

            plt.figure(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
            st.pyplot(plt)
        except:
            st.error("Erro ao gerar o gráfico.")
    else:
        st.info("📎 Aguarde os dados para mostrar o gráfico.")

# Exemplo de dados
st.markdown("""game_id,server,receiver,server_points,receiver_points,server_aces,server_double_faults,server_1st_serve_pct,game_winner,break_occurred
1,Nadal,Djokovic,4,2,1,0,68,Nadal,0
2,Djokovic,Nadal,2,4,2,1,62,Nadal,1""")
---

### 📌 Exemplo de dados válidos:
