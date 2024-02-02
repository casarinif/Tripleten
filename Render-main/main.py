import pandas as pd
import streamlit as st

# Carregue o conjunto de dados
df = pd.read_csv("data.csv")

# Exiba um título
st.title("Meu aplicativo Render")

# Exiba o conjunto de dados
st.table(df)

# Adicione um widget de seleção
option = st.selectbox("Selecione uma coluna:", df.columns)

# Exiba a coluna selecionada
st.write(df[option])

