import streamlit as st
import pandas as pd
import numpy as np

# Título da aplicação
st.title("Minha Primeira Aplicação com Streamlit 🎉")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Slider para escolher um número
numero = st.slider("Escolha um número:", 1, 100, 10)

# Botão
if st.button("Gerar dados"):
    st.write(f"Olá, **{nome}**! 👋 Você escolheu o número {numero}.")

    # Criando dados aleatórios
    dados = pd.DataFrame(
        np.random.randn(numero, 2),
        columns=["X", "Y"]
    )

    # Mostrando tabela
    st.dataframe(dados)

    # Mostrando gráfico
    st.line_chart(dados)
