import streamlit as st
st.title("problema terreno")
#entrada de dados
st.write("Digite a largura do terreno")
largura = st.number_input("Largura (m)")
st.write("Digite o comprimento do terreno em metros")
comprimento = st.number_input("comprimento (m)")
st.write("digite o valor do m²")
valor_m2 = st.number_input("valor do m² (R$)")
area = largura * comprimento
preço = area * valor_m2
st.write(f"A área do terreno é de {area} metros quadrados.")
