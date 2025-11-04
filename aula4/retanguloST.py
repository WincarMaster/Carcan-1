import streamlit as st
st.title("Problema Retangulo")
base = st.number_input("Digite a altura a base do retangulo")
altura = st.number_input("Digite a altura do retangulo")
area = base * altura
perimetro = 2 * base + altura * 2 
diagonal = (base**2 + altura**2)**0.5
st.write(f"A area do retangulo é: {area}")
st.write(f"O perimetro do retangulo é {perimetro}")
st.write(f"Adiagonal do retangulo é: {diagonal}")