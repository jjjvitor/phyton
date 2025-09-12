import streamlit as st
import time

st.title("verificando")

st.header("exercicio verificando")
st.write("escrever um programa de computador que solicite do usuario 4 notas e, ao final apresente a media")

quantidades_notas = 4
soma = 0

for i in range(quantidades_notas):
    nota = st.number_input (f"digite a {i+1}ª nota: ")
    soma = soma + nota

media = soma / quantidades_notas

if st.button("mostrar resultado"):
    st.info(f"media: {media}")
    


