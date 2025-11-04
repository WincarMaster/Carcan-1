import streamlit as st
#Problema duração de tempo
TITULO = "Calculadora duração de tempo"
st.title(TITULO)
#entrada de dados
tempo = st.number_input("Digite o tempo em segundos")
#processamento de dados
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60
#saida de dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos")
st.markdown("<h2 style='text-align: left;'>Resultados:</h2>", unsafe_allow_html=True)
st.write(f"O tempo em horas é: {horas:.0f}")
st.write(f"O tempo em minutos é: {minutos:.0f}")
st.write(f"O tempo em segundos é: {segundos:.0f}")