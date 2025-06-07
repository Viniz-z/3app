import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Título e descrição
st.title("Árvore de Classificação de Clientes")
st.write("Este é um exemplo simples de classificação usando árvore de decisão.")

# Dados de exemplo
data = {
    "Idade": [25, 30, 35, 40, 45, 50, 55, 60],
    "Gênero": [0, 1, 0, 1, 0, 1, 0, 1],
    "Renda": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    "Categoria": [0, 0, 1, 1, 2, 2, 3, 3]
}
df = pd.DataFrame(data)

# Mostrar os dados no app
with st.expander("Visualizar dados de exemplo"):
    st.dataframe(df)

# Separar X e y
X = df[["Idade", "Gênero", "Renda"]]
y = df["Categoria"]

# Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=False)

# Mostrar métricas
st.subheader("Desempenho do Modelo")
st.write(f"**Acurácia:** {accuracy:.2f}")
st.text("Relatório de Classificação:")
st.text(report)

# Mostrar visualização da árvore
st.subheader("Visualização da Árvore de Decisão")
fig, ax = plt.subplots(figsize=(12, 6))
plot_tree(model, feature_names=X.columns, class_names=["A", "B", "C", "D"], filled=True)
st.pyplot(fig)

# Previsão interativa
st.subheader("Faça uma Previsão")
idade = st.number_input("Idade", min_value=0)
genero_input = st.selectbox("Gênero", ["Masculino", "Feminino"])
genero = 0 if genero_input == "Masculino" else 1
renda = st.number_input("Renda", min_value=0)

# Dicionário de categorias
categorias = {0: "Categoria A", 1: "Categoria B", 2: "Categoria C", 3: "Categoria D"}

# Botão de previsão
if st.button("Fazer previsão"):
    prediction = model.predict([[idade, genero, renda]])
    st.success(f"A categoria prevista é: {categorias[prediction[0]]}")
