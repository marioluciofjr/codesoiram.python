!pip install -q -U streamlit

import streamlit as st

st.title("Calculadora de Tabuada")

tabuada = st.number_input("Digite a tabuada:", min_value=1, step=1, value=2)
quantidade_max = st.number_input("Digite a quantidade máxima multiplicada:", min_value=1, step=1, value=10)

st.write("\n")

range_max = tabuada * quantidade_max + 1
counter = 0

for i in range(tabuada, range_max, tabuada):
    counter = counter + 1
    st.write(tabuada, "*", counter, "= ", i)
