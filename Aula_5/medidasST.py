#problema medidas
import streamlit as st
import math as mt
TITULO = "Cálculo de área de um quadrado, triangulo e trapézio"
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
#Entrada de dados
medidaA = st.number_input("Inserir a medida A:")
medidaB = st.number_input("Inserir a medida B:")
medidaC = st.number_input("Inserir a medida C:")
areaQuadrado = mt.pow (medidaA,2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB) / 2
#saida de dados
st.markdown("<h2 style='tex-align: lft;'>Resultados:</h2>", unsafe_allow_html=True)
st.write(f"A área do Quadrado é :{areaQuadrado:.4f}")
st.write(f"A área do Triangulo é :{areaTriangulo:.4f}")
st.write(f"A área do Trapezio é :{areaTrapezio:.4f}")