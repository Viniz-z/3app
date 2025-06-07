import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Título
st.title("Comparação de Árvores de Decisão")
st.write("Vamos comparar o desempenho de dois modelos de árvore de decisão com diferentes configurações.")

# Dados de exemplo
data = {
    "Idade": [25, 30, 35, 40, 45, 50, 55, 60],
    "Gênero": [0, 1, 0, 1, 0, 1, 0, 1],
    "Renda": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    "Categoria": [0, 0, 1, 1, 2, 2, 3, 3]
}
df = pd.DataFrame(data)

with st.expander("Visualizar dados de exemplo"):
    st.dataframe(df)

# Features e target
X = df[["Idade", "Gênero", "Renda"]]
y = df["Categoria"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Sidebar para hiperparâmetros
st.sidebar.title("Configurações dos Modelos")

st.sidebar.subheader("Modelo 1")
max_depth1 = st.sidebar.slider("Profundidade máxima (Modelo 1)", 1, 10, 3)

st.sidebar.subheader("Modelo 2")
max_depth2 = st.sidebar.slider("Profundidade máxima (Modelo 2)", 1, 10, 5)

# Criar duas colunas
col1, col2 = st.columns(2)

# ===== Modelo 1 =====
with col1:
    st.subheader("Modelo 1")
    model1 = DecisionTreeClassifier(max_depth=max_depth1, random_state=42)
    model1.fit(X_train, y_train)
    y_pred1 = model1.predict(X_test)
    acc1 = accuracy_score(y_test, y_pred1)
    st.write(f"Acurácia: **{acc1:.2f}**")
    st.text("Relatório:")
    st.text(classification_report(y_test, y_pred1))

    fig1, ax1 = plt.subplots()
    plot_tree(model1, feature_names=X.columns, class_names=["A", "B", "C", "D"], filled=True)
    st.pyplot(fig1)

# ===== Modelo 2 =====
with col2:
    st.subheader("Modelo 2")
    model2 = DecisionTreeClassifier(max_depth=max_depth2, random_state=42)
    model2.fit(X_train, y_train)
    y_pred2 = model2.predict(X_test)
    acc2 = accuracy_score(y_test, y_pred2)
    st.write(f"Acurácia: **{acc2:.2f}**")
    st.text("Relatório:")
    st.text(classification_report(y_test, y_pred2))

    fig2, ax2 = plt.subplots()
    plot_tree(model2, feature_names=X.columns, class_names=["A", "B", "C", "D"], filled=True)
    st.pyplot(fig2)

# Comparação direta
st.markdown("---")
st.subheader("Comparação Final")
st.write(f"Acurácia Modelo 1: **{acc1:.2f}** | Profundidade: {max_depth1}")
st.write(f"Acurácia Modelo 2: **{acc2:.2f}** | Profundidade: {max_depth2}")
melhor = "Modelo 1" if acc1 > acc2 else "Modelo 2" if acc2 > acc1 else "Empate"
st.success(f"Modelo com melhor desempenho: **{melhor}**")
