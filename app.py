import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar os dados
st.title("Árvore de Classificação")
st.write("Exemplo de classificação de clientes")

# Criar um dataframe de exemplo
data = {
    "Idade": [25, 30, 35, 40, 45, 50, 55, 60],
    "Gênero": [0, 1, 0, 1, 0, 1, 0, 1],
    "Renda": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    "Categoria": [0, 0, 1, 1, 2, 2, 3, 3]
}

df = pd.DataFrame(data)

# Dividir os dados em conjuntos de treinamento e teste
X = df[["Idade", "Gênero", "Renda"]]
y = df["Categoria"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Criar uma interface Streamlit
st.write("Modelo treinado com precisão:", accuracy)
st.write("Relatório de classificação:")
st.write(report)

# Criar um formulário para fazer previsões
st.write("Faça uma previsão")
idade = st.number_input("Idade", min_value=0)
genero = st.selectbox("Gênero", [0, 1])
renda = st.number_input("Renda", min_value=0)

if st.button("Fazer previsão"):
    # Fazer a previsão
    prediction = model.predict([[idade, genero, renda]])
    st.write("A categoria prevista é:", prediction[0])
