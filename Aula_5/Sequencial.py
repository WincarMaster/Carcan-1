import streamlit as st
#Problema duração de tempo
TITULO = "Atividade 01 - Sequencial"
st.title(TITULO)
#entrada de dados
preco = st.number_input("Preço unitario do produto:",min_value=0.0,step=1.0,)
quantidade = st.number_input("Quantidade comprada:",min_value=0.0,step=1.0,)
dinheiro = st.number_input("Dinheiro recebido:",min_value=0.0,step=1.0,)
troco = dinheiro - (preco * quantidade)
st.write(f"O troco é: {troco:.2f}")